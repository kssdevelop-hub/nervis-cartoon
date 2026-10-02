import json
import os
import shutil
import time
from pathlib import Path
from typing import Any, Dict, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = PROJECT_ROOT / "generated_images"
RENDER_ROOT = PROJECT_ROOT / "rendered_video"


class AnimationClipConfig:
    def __init__(self, clip_id: str, name: str, duration_sec: int, source_images: List[str], prompt: str, output_name: str):
        self.clip_id = clip_id
        self.name = name
        self.duration_sec = duration_sec
        self.source_images = source_images
        self.prompt = prompt
        self.output_name = output_name


CLIP_CONFIGS: List[AnimationClipConfig] = [
    AnimationClipConfig(
        "clip_01",
        "Bear wakes up in den",
        4,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_sleeping_*.png"),
            str(OUTPUT_ROOT / "characters" / "mishka_waking_*.png"),
        ],
        "young brown bear slowly wakes up in cozy den, yawns, stretches, soft morning light, gentle camera move, smooth cinematic cartoon motion, warm forest colors",
        "clip_01_bear_wakes_up.mp4",
    ),
    AnimationClipConfig(
        "clip_02",
        "Bear exits den",
        5,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_exiting_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_den_entrance_*.png"),
        ],
        "young brown bear steps out of cozy den, looks around at spring forest, snow melting, soft golden sunrise, gentle cinematic camera drift, cozy cartoon animation",
        "clip_02_bear_exits_den.mp4",
    ),
    AnimationClipConfig(
        "clip_03",
        "Bear walks through forest",
        5,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_walking_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_path_spring_*.png"),
        ],
        "brown bear walks through spring forest path, first flowers emerge, soft sunlight, camera follows behind, natural walking motion, warm cozy cartoon mood",
        "clip_03_bear_walks.mp4",
    ),
    AnimationClipConfig(
        "clip_04",
        "Bear by stream",
        4,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_stream_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_stream_*.png"),
        ],
        "brown bear stands by crystal stream, looks with wonder at flowing water, soft sunlight reflects on water, gentle camera close-up, calm cinematic animation",
        "clip_04_bear_by_stream.mp4",
    ),
    AnimationClipConfig(
        "clip_05",
        "Bear looks at sun",
        4,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_sun_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_winter_dawn_*.png"),
        ],
        "brown bear raises head to sunrise, joyful realization that spring has come, warm golden light fills forest, uplifting cinematic camera push-in",
        "clip_05_bear_sunrise.mp4",
    ),
    AnimationClipConfig(
        "clip_06",
        "Finding small animal tracks",
        4,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_walking_*.png"),
            str(OUTPUT_ROOT / "characters" / "small_animal_scared_*.png"),
        ],
        "brown bear follows tiny animal tracks in snow, curious expression, soft suspense, close camera, gentle animation and forest ambience, cozy cartoon style",
        "clip_06_tracks.mp4",
    ),
    AnimationClipConfig(
        "clip_07",
        "Meeting small forest animal",
        5,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_exiting_*.png"),
            str(OUTPUT_ROOT / "characters" / "small_animal_scared_*.png"),
        ],
        "brown bear meets small fox or rabbit in spring forest, gentle eye contact, calm emotional exchange, soft lighting, warm and believable cartoon interaction",
        "clip_07_meeting.mp4",
    ),
    AnimationClipConfig(
        "clip_08",
        "Helping the animal",
        5,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_helping_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_glade_bloom_*.png"),
        ],
        "brown bear gently helps small animal out of snow, caring expression, warm spring glade, soft heroic but gentle motion, emotional heartfelt cartoon animation",
        "clip_08_helping.mp4",
    ),
    AnimationClipConfig(
        "clip_09",
        "Final smile",
        4,
        [
            str(OUTPUT_ROOT / "characters" / "mishka_smile_camera_*.png"),
            str(OUTPUT_ROOT / "backgrounds" / "bg_forest_glade_bloom_*.png"),
        ],
        "brown bear smiles directly at camera in a glowing spring forest, warm joy, beautiful peaceful ending, cinematic close-up, soft cartoon lighting",
        "clip_09_final_smile.mp4",
    ),
]


def collect_image_paths(patterns: List[str]) -> List[str]:
    files: List[str] = []
    for pattern in patterns:
        matches = sorted(Path().glob(pattern))
        if not matches:
            print(f"[WARN] No images found for pattern: {pattern}")
            continue
        for match in matches:
            files.append(str(match))
    return files


def ensure_tools() -> None:
    tool_checks = [
        ("ffmpeg", "ffmpeg --version"),
        ("python", "python --version"),
    ]
    for name, cmd in tool_checks:
        if name == "ffmpeg":
            import subprocess
            res = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
            if res.returncode != 0:
                raise RuntimeError("ffmpeg not found. Install FFmpeg and ensure it is in PATH.")


def build_clip_sequence(clips: List[AnimationClipConfig]) -> List[str]:
    RENDER_ROOT.mkdir(parents=True, exist_ok=True)
    clip_files: List[str] = []

    for clip in clips:
        source_files = collect_image_paths(clip.source_images)
        if not source_files:
            print(f"[WARN] Skip clip {clip.clip_id}: no source images found")
            continue

        staging_dir = PROJECT_ROOT / "temp_clip_frames" / clip.clip_id
        staging_dir.mkdir(parents=True, exist_ok=True)

        for idx, src in enumerate(source_files[:8]):
            dest = staging_dir / f"frame_{idx:03d}.png"
            shutil.copy2(src, dest)

        frame_pattern = str(staging_dir / "frame_%03d.png")
        out_path = str(RENDER_ROOT / clip.output_name)

        cmd = [
            "ffmpeg",
            "-y",
            "-framerate", "2",
            "-i", frame_pattern,
            "-pix_fmt", "yuv420p",
            "-c:v", "libx264",
            "-movflags", "+faststart",
            "-t", str(clip.duration_sec),
            out_path,
        ]

        print(f"[RUN] {clip.name}")
        print("CMD:", " ".join(cmd))
        import subprocess
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(res.stderr)
            raise RuntimeError(f"FFmpeg failed for {clip.name}")

        clip_files.append(out_path)
        print(f"[OK] Created clip: {out_path}")

    return clip_files


def concat_clips(clips: List[str], final_name: str = "mishka_pilot_30sec.mp4") -> str:
    if not clips:
        raise RuntimeError("No clips to concatenate.")

    concat_list = PROJECT_ROOT / "temp_concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for clip in clips:
            f.write(f"file '{clip}'\n")

    output_path = str(RENDER_ROOT / final_name)
    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ]

    print("[RUN] Concatenating final video")
    import subprocess
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stderr)
        raise RuntimeError("FFmpeg concat failed")

    print(f"[OK] Final video created: {output_path}")
    return output_path


if __name__ == "__main__":
    ensure_tools()
    clips = build_clip_sequence(CLIP_CONFIGS)
    final = concat_clips(clips, "mishka_pilot_30sec.mp4")
    print(f"\nFINAL VIDEO: {final}")
    print("READY FOR REVIEW")

import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict, Optional, List

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY")
RUNWAY_API_BASE_URL = os.getenv("RUNWAY_API_BASE_URL", "https://api.dev.runwayml.com")
GENERATION_MODEL = os.getenv("GENERATION_MODEL", "gpt_image_2")


class RunwayAPIError(RuntimeError):
    pass


class RunwayAPIClient:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key or RUNWAY_API_KEY
        if not self.api_key:
            raise RunwayAPIError("RUNWAY_API_KEY is not configured in .env")

        self.base_url = (base_url or RUNWAY_API_BASE_URL).rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Runway-Version": "2024-11-06",
            }
        )

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        url = f"{self.base_url.rstrip('/')}/v1{path}"

        print(f"\n[DEBUG] Request:")
        print(f"  URL: {url}")
        print(f"  Method: {method}")
        if json_body:
            print(f"  Body: {json.dumps(json_body, indent=2)}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                timeout=timeout,
            )
        except requests.RequestException as exc:
            raise RunwayAPIError(f"Request failed: {exc}")

        print(f"\n[DEBUG] Response Status: {response.status_code}")

        try:
            payload = response.json()
        except ValueError:
            payload = {"raw": response.text}

        if response.status_code < 400:
            return payload

        print(f"[DEBUG] Error Details: {json.dumps(payload, indent=2, ensure_ascii=False)}")
        message = payload.get("error") or payload.get("message") or response.text
        raise RunwayAPIError(f"Runway API error {response.status_code}: {message}")

    def text_to_image(self, prompt_text: str, model: Optional[str] = None, ratio: str = "1920:1088", **extra_fields) -> Dict[str, Any]:
        """Generate an image from text prompt using gpt_image_2."""
        model = model or GENERATION_MODEL
        body = {
            "model": model,
            "promptText": prompt_text,
            "ratio": ratio,
            **extra_fields
        }
        return self._request("POST", "/text_to_image", json_body=body)

    def get_task(self, task_id: str) -> Dict[str, Any]:
        """Get task status and results."""
        return self._request("GET", f"/tasks/{task_id}")

    def wait_for_task(
        self,
        task_id: str,
        *,
        poll_interval: int = 5,
        timeout_seconds: int = 600,
    ) -> Dict[str, Any]:
        """Poll task until completion."""
        deadline = time.time() + timeout_seconds
        while time.time() < deadline:
            task = self.get_task(task_id)
            status = str(task.get("status", "")).lower()
            print(f"[POLL] Task {task_id}: {status}")
            if status in {"succeeded", "completed"}:
                return task
            if status in {"failed", "cancelled", "canceled"}:
                raise RunwayAPIError(f"Task failed with status: {status}")
            time.sleep(poll_interval)
        raise TimeoutError(f"Task {task_id} did not finish within {timeout_seconds} seconds")

    @staticmethod
    def download_image(url: str, filename: str, output_dir: str = "generated_images") -> str:
        """Download image from URL and save locally."""
        try:
            print(f"\n[DOWNLOAD] Downloading image from URL...")
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # Create output directory if it doesn't exist
            output_path = PROJECT_ROOT / output_dir
            output_path.mkdir(exist_ok=True)

            filepath = output_path / filename
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Image saved to: {filepath}")
            return str(filepath)
        except Exception as e:
            print(f"✗ Failed to download image: {e}")
            raise


# ============================================================================
# GENERATION PROMPTS - ALL ORGANIZED
# ============================================================================

GENERATION_JOBS = {
    "backgrounds": [
        {
            "id": "bg_forest_winter_dawn",
            "name": "Forest Winter Dawn",
            "prompt": "misty dark pine forest at dawn, snow covered ground and trees, cold blue winter light, fog and mist thick, bear den barely visible, cinematic wide landscape shot, detailed forest environment, magical misty atmosphere, no animals or characters, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
        {
            "id": "bg_bear_den_interior",
            "name": "Bear Den Interior",
            "prompt": "cozy warm bear den interior, wooden logs and earth walls, golden morning light coming from entrance, soft comfortable den, no bear, cinematic interior lighting, detailed den environment, welcoming warm atmosphere, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
        {
            "id": "bg_forest_den_entrance",
            "name": "Forest Den Entrance Spring",
            "prompt": "forest den entrance at spring dawn, melting snow, first green shoots, golden morning light breaking through trees, transition from winter to spring visible, detailed forest environment, cinematic landscape composition, magical spring beginning, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
        {
            "id": "bg_forest_path_spring",
            "name": "Forest Path Spring",
            "prompt": "forest path winding through spring forest, melting snow, first flowers and green shoots everywhere, golden warm sunlight through trees, vibrant awakening nature, detailed forest flora, cinematic composition, rich spring colors, magical spring atmosphere, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
        {
            "id": "bg_forest_stream",
            "name": "Forest Stream Spring",
            "prompt": "clear spring stream flowing fast from melting snow, crystal water reflecting golden sunlight, smooth river rocks, lush green forest around, detailed water effects, cinematic landscape, peaceful spring water sounds, magical fresh water environment, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
        {
            "id": "bg_forest_glade_bloom",
            "name": "Forest Glade Spring Bloom",
            "prompt": "beautiful forest glade full of spring flowers blooming, green shoots, golden warm sunlight beams through trees, water droplets sparkling, rich detailed spring flora, butterflies and birds in air, cinematic magical landscape, vibrant warm spring colors, peaceful nature symphony feeling, 1920x1088 aspect ratio",
            "type": "background",
            "output_dir": "generated_images/backgrounds",
        },
    ],
    "characters": [
        {
            "id": "mishka_sleeping",
            "name": "Mishka - Sleeping in Den",
            "prompt": "young brown bear sleeping in cozy den, soft fur, round gentle face, big kind eyes, large paws, peaceful expression, snow visible at den entrance, golden morning light, cartoon style, highly detailed, soft animation ready, warm honey brown colors, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_waking",
            "name": "Mishka - Waking Up",
            "prompt": "young brown bear waking up in den, stretching, yawning wide, eyes opening sleepily, soft fur, round face, gentle expression, morning light, cartoon style, highly detailed, animated pose, warm colors, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_exiting",
            "name": "Mishka - Exiting Den",
            "prompt": "young brown bear exiting den entrance, looking around curiously, slightly surprised expression, standing on hind legs or four legs, soft brown fur, morning light, forest background with melting snow, cartoon animation style, highly detailed, dynamic pose, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_walking",
            "name": "Mishka - Walking Forest Path",
            "prompt": "young brown bear walking on forest path through melting snow, happy expression, soft fur, natural gait, warm spring atmosphere, first green shoots emerging, golden light, cartoon animation style, dynamic motion ready, highly detailed, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_stream",
            "name": "Mishka - At Stream Amazed",
            "prompt": "young brown bear kneeling by crystal clear spring stream, water flowing fast, amazed wonder-struck expression, watching water intently, soft brown fur, warm golden sunlight reflecting on water, detailed forest background, cartoon style, cinematic lighting, highly detailed, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_sun",
            "name": "Mishka - Looking at Sun",
            "prompt": "young brown bear standing with raised head looking at golden sunrise sun, forest background full of spring light, warm colors, expression of realization and joy, majestic forest landscape, cartoon animation style, cinematic wide shot, triumph moment, highly detailed, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_helping",
            "name": "Mishka - Helping Small Creature",
            "prompt": "young brown bear gently helping small animal, protective caring pose, forest glade with spring flowers, warm golden sunlight beams, water droplets sparkling, emotional heartwarming moment, cartoon animation style, cinematic composition, soft warm colors, highly detailed, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "mishka_smile_camera",
            "name": "Mishka - Smiling at Camera",
            "prompt": "young brown bear smiling warmly directly at camera, surrounded by vibrant spring forest in full bloom, golden bright sunlight, happy peaceful expression, majestic spring landscape, cinematic close-up, cartoon animation style, triumphant joyful mood, beautiful warm colors, highly detailed, 1920x1088 aspect ratio",
            "type": "character",
            "output_dir": "generated_images/characters",
        },
        {
            "id": "small_animal_scared",
            "name": "Small Animal - Scared from Bushes",
            "prompt": "small cute red fox kit or rabbit appearing from bushes, scared cautious expression, soft fur, detailed face, spring forest setting, detailed animation style, cartoon matching main character, cinematic lighting, highly detailed, 1920x1088 aspect ratio",
            "type": "secondary_character",
            "output_dir": "generated_images/characters",
        },
    ],
}

# ============================================================================
# MISHKA PILOT GENERATION MANAGER
# ============================================================================

class MishkaPilotGenerator:
    def __init__(self, client: RunwayAPIClient):
        self.client = client
        self.generated_images = {}
        self.failed_tasks = []
        self.output_dir = PROJECT_ROOT / "generated_images"
        self.output_dir.mkdir(exist_ok=True)

    def generate_all_images(self) -> Dict[str, Any]:
        """Generate all background and character images for Mishka pilot."""
        print("\n" + "=" * 80)
        print("MISHKA PILOT - IMAGE GENERATION STARTING")
        print("=" * 80)

        # Generate backgrounds
        print("\n[STEP 1/2] Generating Background Images...")
        print("-" * 80)
        for bg in GENERATION_JOBS["backgrounds"]:
            self._generate_single_image(bg)

        # Generate characters
        print("\n[STEP 2/2] Generating Character Images...")
        print("-" * 80)
        for char in GENERATION_JOBS["characters"]:
            self._generate_single_image(char)

        # Summary
        self._print_summary()
        return self.generated_images

    def _generate_single_image(self, job: Dict[str, Any]) -> None:
        """Generate a single image and download it."""
        job_id = job["id"]
        job_name = job["name"]
        prompt = job["prompt"]

        print(f"\n[GENERATING] {job_name} ({job_id})...")

        try:
            # Create task
            result = self.client.text_to_image(
                prompt_text=prompt,
                ratio="1920:1088"
            )

            task_id = result.get("id")
            if not task_id:
                raise RunwayAPIError(f"No task ID returned for {job_name}")

            print(f"[TASK CREATED] Task ID: {task_id}")

            # Wait for completion
            final_result = self.client.wait_for_task(task_id, timeout_seconds=600)
            outputs = final_result.get("output", [])

            if not outputs:
                raise RunwayAPIError(f"No output from task {task_id}")

            url = outputs[0]
            print(f"[COMPLETE] Output URL: {url}")

            # Download image
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{job_id}_{timestamp}.png"
            output_subdir = job.get("output_dir", "generated_images")

            # Create subdirectory
            sub_path = PROJECT_ROOT / output_subdir
            sub_path.mkdir(parents=True, exist_ok=True)

            local_path = self._download_image(url, filename, output_subdir)

            self.generated_images[job_id] = {
                "name": job_name,
                "type": job.get("type"),
                "task_id": task_id,
                "url": url,
                "local_path": local_path,
                "status": "success",
            }

            print(f"[SUCCESS] Image saved: {local_path}")

        except Exception as e:
            print(f"[ERROR] Failed to generate {job_name}: {e}")
            self.failed_tasks.append({
                "id": job_id,
                "name": job_name,
                "error": str(e),
            })
            self.generated_images[job_id] = {
                "name": job_name,
                "type": job.get("type"),
                "status": "failed",
                "error": str(e),
            }

    def _download_image(self, url: str, filename: str, output_dir: str) -> str:
        """Download image from URL."""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            full_path = PROJECT_ROOT / output_dir
            full_path.mkdir(parents=True, exist_ok=True)

            filepath = full_path / filename
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"[DOWNLOAD] Saved to: {filepath}")
            return str(filepath)
        except Exception as e:
            print(f"[DOWNLOAD ERROR] {e}")
            raise

    def _print_summary(self) -> None:
        """Print generation summary."""
        print("\n" + "=" * 80)
        print("GENERATION SUMMARY")
        print("=" * 80)

        success_count = sum(1 for v in self.generated_images.values() if v["status"] == "success")
        failed_count = sum(1 for v in self.generated_images.values() if v["status"] == "failed")

        print(f"\n✓ Successfully generated: {success_count}")
        print(f"✗ Failed: {failed_count}")
        print(f"Total jobs: {len(self.generated_images)}")

        if self.failed_tasks:
            print("\n[FAILED TASKS]")
            for task in self.failed_tasks:
                print(f"  - {task['name']} ({task['id']}): {task['error']}")

        print(f"\n[OUTPUT DIRECTORY] {self.output_dir}")
        print("\n[GENERATED FILES]")
        for job_id, info in self.generated_images.items():
            status_icon = "✓" if info["status"] == "success" else "✗"
            print(f"  {status_icon} {info['name']}")
            if info["status"] == "success":
                print(f"     Path: {info['local_path']}")

        print("\n" + "=" * 80)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    print("\n" + "=" * 80)
    print("MISHKA PILOT - GENERATION PIPELINE")
    print("=" * 80)
    print(f"Base URL: {RUNWAY_API_BASE_URL}")
    print(f"Model: {GENERATION_MODEL}")
    print(f"API Key: {RUNWAY_API_KEY[:20]}...")
    print("=" * 80)

    try:
        client = RunwayAPIClient()
        generator = MishkaPilotGenerator(client)

        # Generate all images
        generated = generator.generate_all_images()

        print("\n✓ GENERATION PIPELINE COMPLETE!")
        print(f"Generated {len([v for v in generated.values() if v['status'] == 'success'])} images")

    except Exception as e:
        print(f"\n✗ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()

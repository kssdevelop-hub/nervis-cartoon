import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict, Optional

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
        """
        Generate an image from text prompt using gpt_image_2.
        
        Valid ratios for gpt_image_2:
        1920:1088, 1920:1280, 1920:1440, 1920:1536, 1920:1920,
        1536:1920, 1440:1920, 1280:1920, 1088:1920, etc.
        or "auto"
        """
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
    def download_image(url: str, filename: str) -> str:
        """Download image from URL and save locally."""
        try:
            print(f"\n[DOWNLOAD] Downloading image from URL...")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Create output directory if it doesn't exist
            output_dir = PROJECT_ROOT / "generated_images"
            output_dir.mkdir(exist_ok=True)
            
            filepath = output_dir / filename
            with open(filepath, "wb") as f:
                f.write(response.content)
            
            print(f"✓ Image saved to: {filepath}")
            return str(filepath)
        except Exception as e:
            print(f"✗ Failed to download image: {e}")
            raise


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    print("=" * 70)
    print("Runway API Client - Text to Image")
    print("=" * 70)
    print(f"Base URL: {RUNWAY_API_BASE_URL}")
    print(f"Model: {GENERATION_MODEL}")
    print(f"API Key: {RUNWAY_API_KEY[:20]}...")
    print("=" * 70)

    client = RunwayAPIClient()
    
    prompt_text = "cartoon bear character, sitting in forest, bright colors, cinematic lighting, cartoon style"
    
    try:
        print(f"\nGenerating image with prompt:\n  {prompt_text}\n")
        result = client.text_to_image(prompt_text=prompt_text, ratio="1920:1088")
        print("\n✓ Generation task created successfully!")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        task_id = result.get("id")
        if task_id:
            print(f"\n→ Waiting for task {task_id} to complete...")
            print("  (This may take a few minutes)")
            final_result = client.wait_for_task(task_id, timeout_seconds=600)
            print("\n✓ Task completed!")
            print(json.dumps(final_result, ensure_ascii=False, indent=2))
            
            outputs = final_result.get("output", [])
            if outputs:
                url = outputs[0]
                print(f"\n✓ Generated image URL:\n  {url}")
                
                # Download and save locally
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"generated_{timestamp}.png"
                local_path = client.download_image(url, filename)
                print(f"✓ Local path: {local_path}")
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()

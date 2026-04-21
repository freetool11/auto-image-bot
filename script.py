import requests
import os
import time
from datetime import datetime

# ✅ FIXED MODEL (IMPORTANT CHANGE)
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
    "Content-Type": "application/json"
}


def generate_image(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

    # ⏳ Model loading (first time)
    if response.status_code == 503:
        print("⏳ Model loading... waiting 10 seconds")
        time.sleep(10)
        return generate_image(prompt)

    # ❌ Error handling
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None

    return response.content


# 📁 Create folder
today = datetime.now().strftime("%Y-%m-%d")
output_dir = f"images/{today}"
os.makedirs(output_dir, exist_ok=True)

# 📄 Load prompts
with open("prompts.txt", "r") as f:
    prompts = [p.strip() for p in f if p.strip()]

print(f"Loaded {len(prompts)} prompts")

# 🔁 Generate images
for i, prompt in enumerate(prompts):
    try:
        print(f"🎨 Generating {i+1}: {prompt}")

        image = generate_image(prompt)

        if image is None:
            print("⚠️ Skipping image due to error")
            continue

        filename = f"{output_dir}/img_{i+1}.png"

        with open(filename, "wb") as f:
            f.write(image)

        print(f"✅ Saved: {filename}")

        time.sleep(5)

    except Exception as e:
        print("❌ Exception:", e)
        time.sleep(10)

print("🎉 Done generating images")

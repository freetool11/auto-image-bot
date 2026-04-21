import requests
import os
import time
from datetime import datetime

def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    response = requests.get(url)
    return response.content

# Create folder
today = datetime.now().strftime("%Y-%m-%d")
output_dir = f"images/{today}"
os.makedirs(output_dir, exist_ok=True)

# Load prompts
with open("prompts.txt", "r") as f:
    prompts = [p.strip() for p in f if p.strip()]

print(f"Loaded {len(prompts)} prompts")

for i, prompt in enumerate(prompts):
    try:
        print(f"🎨 Generating {i+1}: {prompt}")

        image = generate_image(prompt)

        filename = f"{output_dir}/img_{i+1}.png"

        with open(filename, "wb") as f:
            f.write(image)

        print(f"✅ Saved: {filename}")

        time.sleep(2)

    except Exception as e:
        print("❌ Exception:", e)
        time.sleep(5)

print("🎉 Done generating images")

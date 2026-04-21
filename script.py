import requests
import os
import time
import random
from datetime import datetime

def generate_image(prompt):
    # 🎯 Improve prompt quality
    enhanced_prompt = f"{prompt}, ultra realistic, 4k, highly detailed, cinematic lighting, sharp focus"

    # 🎲 Random seed for variety
    seed = random.randint(1, 100000)

    # 📸 Higher resolution + better output
    url = f"https://image.pollinations.ai/prompt/{enhanced_prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}"

    response = requests.get(url)
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

        filename = f"{output_dir}/img_{i+1}.png"

        with open(filename, "wb") as f:
            f.write(image)

        print(f"✅ Saved: {filename}")

        time.sleep(2)

    except Exception as e:
        print("❌ Exception:", e)
        time.sleep(5)

print("🎉 Done generating images")

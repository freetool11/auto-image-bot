import requests
import os
import time
from datetime import datetime

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    return response.content

# Create folder
today = datetime.now().strftime("%Y-%m-%d")
output_dir = f"images/{today}"
os.makedirs(output_dir, exist_ok=True)

# Load prompts
with open("prompts.txt", "r") as f:
    prompts = [p.strip() for p in f if p.strip()]

for i, prompt in enumerate(prompts):
    try:
        print(f"Generating {i+1}: {prompt}")

        image = generate_image(prompt)

        with open(f"{output_dir}/img_{i+1}.png", "wb") as f:
            f.write(image)

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)

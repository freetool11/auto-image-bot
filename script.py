import google.generativeai as genai
import time
import os
from PIL import Image
from io import BytesIO
from datetime import datetime

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

WIDTH = 1024
HEIGHT = 1024

today = datetime.now().strftime("%Y-%m-%d")
output_dir = f"images/{today}"
os.makedirs(output_dir, exist_ok=True)

with open("prompts.txt", "r") as f:
    prompts = [p.strip() for p in f if p.strip()]

for i, prompt in enumerate(prompts):
    try:
        response = model.generate_content(prompt)

        image_data = response.candidates[0].content.parts[0].inline_data.data

        img = Image.open(BytesIO(image_data))
        img = img.resize((WIDTH, HEIGHT))

        filename = f"{output_dir}/img_{i+1}.png"
        img.save(filename)

        print("Saved:", filename)

        time.sleep(6)

    except Exception as e:
        print("Error:", e)
        time.sleep(20)
from diffusers import StableDiffusionPipeline
# import torch
from PIL import Image
import os

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cpu")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    image_path = os.path.join('media/generated_images', f"{prompt.replace(' ', '_')}.png")
    image.save(image_path)
    return image_path

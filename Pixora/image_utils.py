import os
from diffusers import StableDiffusionPipeline
from PIL import Image
from django.conf import settings

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cpu")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    image_filename = f"{prompt.replace(' ', '_')}.png"
    image_path = os.path.join(settings.MEDIA_ROOT, 'generated_images', image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    image.save(image_path)
    
    return image_path

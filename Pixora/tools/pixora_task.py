from celery import shared_task
from .processing_image import generate_image
from Pixora.models import ImageRequest

@shared_task
def generate_image_task(image_request_id):
    image_request = ImageRequest.objects.get(pk=image_request_id)
    image_path = generate_image(image_request.prompt)
    image_request.image = image_path
    image_request.save()

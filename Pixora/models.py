from django.db import models
from django.contrib.auth.models import User
import uuid

class ImageRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prompt = models.TextField()
    image = models.ImageField(upload_to='generated_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='completed')

    def __str__(self):
        return str(self.id)

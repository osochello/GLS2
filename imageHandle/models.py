from django.db import models
from django.core.files.base import ContentFile

class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshots/')
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, image_data, timestamp):
        screenshot = cls()
        screenshot.image.save(f'screenshot_{timestamp}.png', ContentFile(image_data), save=False)
        screenshot.save()
        return screenshot
from django.db import models
from django.utils import timezone
from PIL import Image


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        self.author

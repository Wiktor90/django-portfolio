from django.db import models
from django.utils import timezone
from PIL import Image


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(default="description", max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    url = models.URLField(max_length=400, default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height >300 or img. width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
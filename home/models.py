from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from PIL import Image


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    accepted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)

    def __str__(self):
        return self.author
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 228 or img.width > 228:
                output_size = (228, 228)
                img_resized = img.resize(output_size,3)
                img_resized.save(self.image.path)



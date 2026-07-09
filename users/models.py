from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#CASCADE means that if the user is deleted, the profile will be deleted too
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_profile = profile.objects.get(pk=self.pk)
                if old_profile.image and old_profile.image.name != self.image.name:
                    if old_profile.image.name != 'default.jpg':
                        old_profile.image.delete(save=False)
            except profile.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)  # open image

        if img.height > 300 or img.width > 300:  # resize the image
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


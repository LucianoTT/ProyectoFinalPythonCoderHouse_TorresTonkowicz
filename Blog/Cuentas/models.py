from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='images', null=True, blank = True)
    description = models.TextField()
    social1 = models.URLField(max_length=200)
    social2 = models.URLField(max_length=200)

    def __str__(self):
        #return self.user.username
        return f"{settings.MEDIA_URL}{self.avatar}"

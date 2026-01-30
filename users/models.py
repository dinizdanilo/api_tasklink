from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'usuarios'

    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    xp = models.IntegerField(default=0, verbose_name="Experiência")
    level = models.IntegerField(default=1, verbose_name="Nível")

    def __str__(self):
        return self.username
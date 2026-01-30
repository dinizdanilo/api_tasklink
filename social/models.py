from django.db import models
from django.conf import settings

class StudyGroup(models.Model):
    class Meta:
        db_table = 'grupos_estudo'

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    invite_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    class Meta:
        db_table = 'membros_grupos'
        unique_together = ('user', 'group')

    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('member', 'Membro'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    class Meta:
        db_table = 'mensagens_chat'
        
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
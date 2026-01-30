from django.db import models
from django.conf import settings # Importa o usuário configurado no settings

class Task(models.Model):
    class Meta:
        db_table = 'tarefas'

    STATUS_CHOICES = [
        ('todo', 'A Fazer'),
        ('doing', 'Fazendo'),
        ('done', 'Feito'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

class PomodoroSession(models.Model):
    class Meta:
        db_table = 'sessoes_pomodoro'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    duration_minutes = models.IntegerField(default=25)
    completed_at = models.DateTimeField(auto_now_add=True)

class Deck(models.Model):
    class Meta:
        db_table = 'baralhos_flashcards'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50) # Ex: Inglês, Matemática

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    class Meta:
        db_table = 'cartoes_estudo'
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    front = models.TextField(help_text="A pergunta")
    back = models.TextField(help_text="A resposta")
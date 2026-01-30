from rest_framework import serializers
from .models import Task, FlashcardDeck, Flashcard, PomodoroSession

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']

class FlashcardDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardDeck
        fields = '__all__'

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = '__all__'
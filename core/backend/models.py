from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'conversation_id'], name='unique_conversation_per_user')
        ]

    def __str__(self):
        return f"Conversation {self.conversation_id} for user {self.user.username}"


class Interaction(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction {self.id} in conversation {self.conversation.conversation_id}"
    

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event = models.TextField(blank=True)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
    
    def __str__(self):
        return self.event if self.event else "No event"
    

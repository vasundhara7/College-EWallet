from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    roomname = models.TextField(blank = False)
    rec_name = models.TextField(blank = False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        print(Message.objects.order_by('-timestamp').all()[:10])
        return Message.objects.order_by('-timestamp').all()[0:10]
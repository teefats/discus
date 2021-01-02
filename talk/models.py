from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=200, default='anonymous')
    email = models.EmailField(max_length=200, null = True)
    topic = models.CharField(max_length=200)
    description = models.TextField(max_length=4000, blank =True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    forum = models.ForeignKey(Forum,  blank=True, on_delete=CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)

from django.db import models
from django.utils import timezone

class post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.TextField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True) #true nhi hota kuch True hota hai 
    
    def publish(self):
        self.published_date=timezone.now
        self.save()
    
    def _str_(self):
        return self.title

# Create your models here.

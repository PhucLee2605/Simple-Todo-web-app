from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date',]
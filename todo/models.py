from django.db import models

# Create your models here.
class TodoList(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    def __str__(self):
    	return self.name
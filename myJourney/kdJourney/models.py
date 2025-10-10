from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


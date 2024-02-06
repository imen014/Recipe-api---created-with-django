from django.db import models

class RecipeContainer(models.Model):
    title=models.CharField(max_length=50)
    creator=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    number=models.IntegerField()
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=30, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField(default='')

    def __str__(self):
        return self.title

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import F


# Create your models here.

def validate_rating(value):
    if value < 0 or value > 10:
        raise ValidationError("Rating must be between 0 and 10")


class Author(models.Model):
    Name = models.CharField(max_length=100)
    SureName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name} - {self.SureName}"


class Genre(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name}"


class Book(models.Model):
    Name = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Year = models.IntegerField()
    Genre = models.ManyToManyField(Genre)
    Rating = models.IntegerField(validators=[validate_rating])
    Watch_Count = models.IntegerField(default=0)

    def update_watch_count(self):
        self.Watch_Count += 1
        self.save(update_fields=['Watch_Count'])

    def __str__(self):
        return f"{self.Name} - {self.Slug}"

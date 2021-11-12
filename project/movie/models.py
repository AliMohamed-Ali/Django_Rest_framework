from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)


class CommonInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_poster')
    watch_count = models.IntegerField()
    likes = models.IntegerField()

    class Meta:
        abstract = True
    def __str__(self):
        return self.title

class Movie(CommonInfo):
    pass


class Series(CommonInfo):
    season = models.CharField(max_length=50)
    episode = models.CharField(max_length=50)

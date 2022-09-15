from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(
        max_length=30,
        unique=True
    )


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(
        max_length=30,
        unique=True
    )


class Title(models.Model):
    name = models.CharField(max_length=90)
    year = models.IntegerField()
    description = models.TextField(
        max_length=200,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genre'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='categories'
    )

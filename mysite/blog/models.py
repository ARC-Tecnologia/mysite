from django.db import models


# Create your models here.

STATUS_CHOICES = (
    (0, 'Rascunho'),
    (1, 'Publicado')
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    slug = models.SlugField(max_length=200, unique=True)

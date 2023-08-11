from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Model


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Blog(BaseModel):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=155)
    text = models.TextField()
    user = models.ForeignKey(to="auth.User",
                             on_delete=models.CASCADE,
                             related_name='blogs')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title
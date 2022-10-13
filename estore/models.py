from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    count = models.IntegerField(null=True, default=0)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Contactus(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

class Subscribe(models.Model):
    email = models.EmailField(max_length=255)
    
from django.db import models

class Contact(models.ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class Subscribe(models.ModelForm):
    email = models.EmailField(max_length=255)
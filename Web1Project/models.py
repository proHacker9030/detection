from django.db import models

# Create your models here.


class Method(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='Нет описания')


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    input_image = models.CharField(max_length=255, default='default.jpg')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, default=None)

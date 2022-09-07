from django.db import models


class ApiTest(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image_url = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name

from tabnanny import verbose
from django.db import models

#ip, protocol, country, city, provider, ???(download, upload)???

class visitors(models.Model):
    ipField = models.CharField('IP', max_length=45)
    protocolField = models.CharField('protocol', max_length=4)
    countryField = models.CharField('country', max_length=50)
    cityField = models.CharField('city', max_length=50)
    providerField = models.TextField('provider')
    date = models.CharField('date', max_length=20)
    time = models.CharField('time', max_length=50)
    cookie = models.CharField('cookie', max_length=32)


    def __str__(self):
        return self.ipField

    class Meta:
        verbose_name = 'visitors'
        verbose_name_plural = 'visitors'
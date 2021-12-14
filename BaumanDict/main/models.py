from django.db import models


# Create your models here.

class Entries(models.Model):
    word = models.CharField('eng word', max_length=50)
    translation = models.CharField('ru translation', max_length=100)
    transcription = models.CharField('eng transcription', max_length=50)
    pos = models.CharField('part of speech', max_length=5)
    eng_example = models.CharField('eng example sentence', max_length=250)
    ru_example = models.CharField('ru example sentence', max_length=250)
    module = models.IntegerField('module')

    def __str__(self):
        return self.word

    def getEng(self):
        return self.eng_example

    def getRu(self):
        return self.ru_example

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ["word"]


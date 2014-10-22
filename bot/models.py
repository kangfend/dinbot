from django.db import models
from dinbot.core.utils import Choices


class Remember(models.Model):
    nick = models.CharField(max_length=30)
    word = models.CharField(max_length=50)
    penghubung = models.CharField(max_length=50)
    content = models.TextField()
    channel = models.CharField(max_length=50, blank=True, null=True)
    TYPE = Choices(
        (1, 'arti', 'Arti'),
        (2, 'url', 'URL'),
    )
    type = models.CharField(max_length=20, choices=TYPE)

    def __unicode__(self):
        return self.word


class History(models.Model):
    nick = models.CharField(max_length=30)
    content = models.TextField()
    channel = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.nick


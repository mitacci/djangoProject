from django.db import models


class Profile(models.Model):
    NAME_MAX_LEN = 20
    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    age = models.IntegerField()
    image_url = models.URLField()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    image_url = models.URLField()
    content = models.TextField()

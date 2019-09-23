from django.db import models


class Article(models.Model):
    content = models.TextField('Article Content', blank=True)
    owner = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id)

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    description  = models.TextField(verbose_name='Description')
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return self.title

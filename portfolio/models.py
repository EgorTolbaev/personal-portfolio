from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description  = models.CharField(max_length=250, verbose_name='Description')
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=100,verbose_name=" 电影名")
    description=models.TextField(verbose_name=" 电影简介")
    image=models.ImageField(upload_to="movie/images/",verbose_name=" 电影海报")
    url=models.URLField(blank=True,verbose_name=" 电影资源")

    class Meta:
        verbose_name=" 电影"
        verbose_name_plural=" 电影"

    def __str__(self):
        return self.title


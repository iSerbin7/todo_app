from django.db import models


# Create your models here.

class Post(models.Model):
    title_post = models.CharField('Заголовок поста', max_length=100)
    description_post = models.TextField('Пост')
    author_post = models.CharField('Автор поста', max_length=100)
    date_create_post = models.DateField('Дата публикации')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title_post}, {self.author_post}'
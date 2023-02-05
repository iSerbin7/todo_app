# Generated by Django 4.1.6 on 2023-02-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(max_length=100, verbose_name='Заголовок поста')),
                ('description_post', models.TextField(verbose_name='Пост')),
                ('author_post', models.CharField(max_length=100, verbose_name='Автор поста')),
                ('date_create_post', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
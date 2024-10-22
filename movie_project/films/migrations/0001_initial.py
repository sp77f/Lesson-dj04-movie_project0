# Generated by Django 5.1.2 on 2024-10-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название фильма')),
                ('description', models.CharField(max_length=300, verbose_name='Описание фильма')),
                ('imageurl', models.CharField(max_length=300, verbose_name='Изображение')),
                ('feedback', models.TextField(blank=True, verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]

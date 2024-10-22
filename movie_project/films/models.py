from django.db import models
class Films(models.Model):
    title = models.CharField('Название фильма', max_length=150)
    description = models.CharField('Описание фильма', max_length=300)
    imageurl = models.CharField('Изображение', max_length=300)
    feedback = models.TextField('Отзыв', blank=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


# Create your models here.

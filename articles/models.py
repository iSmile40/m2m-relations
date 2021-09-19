from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField('Scope', related_name='articles', through="ScopesInArticle")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class ScopesInArticle(models.Model):

    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, verbose_name="Раздел", on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name="Основной", default=False)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-is_main', 'scope']

    def __str__(self):
        return f'{self.article}'

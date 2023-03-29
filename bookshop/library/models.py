from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    address = models.CharField(max_length=60, verbose_name='адрес')
    city = models.CharField(max_length=30, verbose_name='город')
    state_province = models.CharField(max_length=30, verbose_name='штат, область')
    country = models.CharField(max_length=30, verbose_name='страна')
    website = models.URLField(blank=True, verbose_name='web-сайт')

    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name='издательство'
        verbose_name_plural='издательства'



class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=40, verbose_name='фамилия')
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name='автор'
        verbose_name_plural='авторы'


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    authors = models.ManyToManyField(Author, verbose_name='автор')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='издательство')
    publication_date = models.DateField(blank=True, null=True, verbose_name='дата публикации')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name='книга'
        verbose_name_plural='книги'

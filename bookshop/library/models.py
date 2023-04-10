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
        ordering = ['-name']



class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=40, verbose_name='фамилия')
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

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
        
        
    class Admin:
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publisher', 'publication_date')
        ordering = ('-publication_date')
        search_fields = ('title')

   def __str__(self):
      return self.title

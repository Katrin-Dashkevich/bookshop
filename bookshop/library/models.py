from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'


class Book(models.Model):
    title = models.CharField(max_length=1000)
    authors = models.ManyToManyField(Author, through="Library")
    publication_date = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.title, self.authors, self.publication_date)    


    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'


class Library(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.author, self.book) 

====================
ИНСТРУКЦИЯ К ПРОЕКТУ

---------------
Проект BookShop:
	Web-приложение для создания онлайн-каталога литературы.
	Проект может быть расширен до интернет-магазина или интернет-библиотеки.

Разработчик:
	Дашкевич Екатерина
	+ 379 29 8587749
	katrindash@gmail.ru

Минимальные требования для работы с проектом:
	Python 3.9		https://www.python.org/
	Django 4.1.4		https://www.djangoproject.com/
	SQLite3			поддерживается Django по умолчанию


--------------
1. Запуск проекта:

1.1 Распаковать проект в отдельный директорий.

1.2 Вызвав системную консоль, перейти в папку с файлом "manage.py". При необходимости ввести команду:
	cd bookshop

1.3 Стартовать Web-сервер, для чего выполнить в консоли команду:
	.\manage.py runserver

1.4 После появления в консоли системного сообщения об успешном запуске Web-сервера стартовать браузер.

1.5 В адресной строке браузера ввести:
	http://127.0.0.1:8000/
в результате загрузится главная страница проекта BookShop.

1.6 Для загрузки Admin-панели в адресной строке браузера ввести:
	http://127.0.0.1:8000/admin/

1.7 Для входа в Admin-панель использовать:
	Имя пользователя:	Admin
	Пароль:			123


-------------------
2. Организация проекта:

2.1 Сервис предоставляет интерфейс для работы с сущностью "Автор". У автора есть:
- имя (максимум 30 символов),
- фамилия (максимум 40  символов).

Описание класса:

	class Author(models.Model):
    		first_name = models.CharField(max_length=30)
    		last_name = models.CharField(max_length=40)

    		def str(self):
        		return '%s %s' % (self.first_name, self.last_name)

    		class Meta:
        		verbose_name='Автор'
        		verbose_name_plural='Авторы'

Примечание 1: класс можно расширить дополнительно - год рождения автора, страна проживания и т.п.

2.2 Сервис предоставляет интерфейс для работы с сущностью "Книга". У книги есть:
- название (максимум 1000 символов),
- один или несколько авторов (отношение многие-ко-многим между авторами и книгами),
- год выпуска.

Описание класса:

	class Book(models.Model):
    		title = models.CharField(max_length=1000)
    		authors = models.ManyToManyField(Author, through="Library")
    		publication_date = models.DateField()

    		def str(self):
        		return '%s %s %s' % (self.title, self.authors, self.publication_date)    

    		class Meta:
        		verbose_name='Книга'
        		verbose_name_plural='Книги'

Примечание 2: поле "authors" имеет тип "ManyToManyField" - у книги может быть один или несколько авторов.
Примечание 3: класс можно расширить дополнительно - издательство, количество страниц, цена, качество обложки, краткая аннотация, отзывы читателей, оценка читателя и т.п.)


-----------------
3. Настройки проекта:

3.1 Файл bookshop\bookshop\settings.py:

	Дополнительное приложение в секции INSTALLED_APPS:
		'library'

	База данных описана в секции DATABASES:
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',

3.2 Файл bookshop\bookshop\urls.py:
	Секция urlpatterns:
		urlpatterns = [
		    path('', views.index, name='index'),
		    path('add', views.add, name='add'),
		    path('authors', views.authors, name='authors'),
		    path('books', views.books, name='books'),
		]

3.1 Файл bookshop\bookshop\views.py:
- главная страница:
	def index(request):
	    return render(request,'index.html')

- страница с формой для добавления новых записей в каталог
	def add(request):
	    return render(request,'add.html')

- авторы, занесённые в базу данных
	def authors(request):
	    return render(request,'authors.html')

- книги, имеющиеся в базе данных
	def books(request):
	    return render(request,'books.html')


-------
4. Ресурсы:
4.1 CSS-стили, шрифты, изображения, скрипты, HTML-шаблоны) размещены в директории:
	bookshop\bookshop\library\static

4.2 Шаблоны размещены в директории:
	bookshop\bookshop\library\templates

4.3 Назначение шаблонов
- add.html	страница для добавления записей в базу данных
- authors.html	авторы
- base.html	главная страница проекта
- books.html	книги, хранящиеся в базе проекта


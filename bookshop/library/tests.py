from django.test import TestCase

from library.models import Author


class LibraryTest(TestCase):

    def test_index(self):
       response = self.client.get('/books')
       self.assertEqual(response.status_code, 200)


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Adam', last_name='Cross')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

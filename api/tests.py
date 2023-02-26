from django.test import TestCase

from todo.models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='the body')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.title, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.body, 'the body')
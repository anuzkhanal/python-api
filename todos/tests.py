from urllib import response
from django.test import TestCase

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from todos.models import Todo


class TodoAPITestCase(APITestCase):
    def create_todo(self):
        todo_test = {"name": "test title", "description": "test description"}
        response = self.client.post(reverse("todos"), todo_test)
        return response

    def authenticate(self):
        self.client.post(
            reverse("register"),
            {"email": "email@gmail.com", "password": "password123"},
        )

        response = self.client.post(
            reverse("login"),
            {"email": "email@gmail.com", "password": "password123"},
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")


class TestTodos(TodoAPITestCase):
    def test_should_not_create_todo_with_no_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        response = self.create_todo()

        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "test title")
        self.assertEqual(response.data["description"], "test description")

    def test_retrieves_all_todos(self):
        self.authenticate()
        response = self.client.get(reverse("todos"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodoDetailAPIView(TodoAPITestCase):
    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.get(reverse("todo", kwargs={"pk": response.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=response.data["id"])
        self.assertEqual(todo.name, res.data["name"])

    def test_update_one_item(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.patch(
            reverse("todo", kwargs={"pk": response.data["id"]}),
            {"name": "new", "description": "new desc", "status": "Ongoing"},
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_todo = Todo.objects.get(id=response.data["id"])
        self.assertEqual(updated_todo.status, "Ongoing")
        self.assertEqual(updated_todo.name, "new")
        self.assertEqual(updated_todo.description, "new desc")

    def test_delete_one_item(self):
        self.authenticate()
        response = self.create_todo()

        prev_db_count = Todo.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        res = self.client.delete(reverse("todo", kwargs={"pk": response.data["id"]}))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Todo.objects.all().count(), 0)

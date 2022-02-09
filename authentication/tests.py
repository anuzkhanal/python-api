from rest_framework.test import APITestCase

from .models import User

# Create your tests here.


class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user("abc@gmail.com", "password123")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "abc@gmail.com")

    def test_create_super_user(self):
        user = User.objects.create_superuser("abc@gmail.com", "password123")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "abc@gmail.com")

    def test_no_email_given(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(email="", password="password123")

    def test_create_super_user_with_is_staff_false(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(
                email="", password="password123", is_staff=False
            )

    def test_create_super_user_with_is_super_user_false(self):
        with self.assertRaisesMessage(
            ValueError, "Superuser must have is_superuser=True."
        ):
            User.objects.create_superuser(
                email="", password="password123", is_superuser=False
            )

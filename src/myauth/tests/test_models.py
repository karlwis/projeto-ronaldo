from django.test import TestCase
from myauth.models import User


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username="karl",
            password="securepassword"
        )

        self.assertEqual(user.username, "karl")
        self.assertTrue(user.check_password("securepassword"))

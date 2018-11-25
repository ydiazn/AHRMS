from django.test import TestCase
from django.test import Client
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import login


c = Client()

class LoginViewTest(TestCase):

    def test_login_redirect_url(self):
        # User creation
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        response = c.post('/accounts/login/', {
            'username': 'john',
            'password': 'johnpassword'
        })

        self.assertRedirects(response, '/core/profile/')
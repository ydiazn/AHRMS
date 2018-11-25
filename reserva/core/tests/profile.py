from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from core import views


c = Client()

class ProfileView(TestCase):

    def test_user_not_logged(self):
        response = c.get('/core/profile/')
        self.assertRedirects(response, '/accounts/login/?next=/core/profile/')

    def test_user_logged(self):
        # User login
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        c.login(username='john', password='johnpassword')

        response = c.get('/core/profile/')
        self.assertEquals(response.status_code, 200)
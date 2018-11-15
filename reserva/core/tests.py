from django.test import TestCase
from django.test import Client
from . import views


c = Client()

class ProfileView(TestCase):

    def test_profile(self):
        response = c.get('/core/profile/')
        self.assertEquals(response.status_code, 200)
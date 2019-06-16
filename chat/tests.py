from django.test import TestCase

from dashboard.models import Profile,User
from django.test.client import Client
from django.urls import reverse

class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='raj', password='root@1234')


    def test_logintest(self):

        response = self.client.get(reverse('chat:index'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,str("/dashboard/login/?next=/chat/"))


    def test_room_redirect(self):
        login=self.client.login(username='raj', password='root@1234')
        self.assertTrue(login)
        response = self.client.get(reverse('chat:index'))
        self.assertEquals(response.url,str(11))


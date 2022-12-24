from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import date



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # login
        response = self.client.post('/login/', **self.credentials)      
        # should be logged in now, fails however
        self.assertFalse(response.context['user'].is_active)


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


# class SignInViewTest(TestCase):

#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test',
#                                                          password='12test12',
#                                                          email='test@example.com')

#     def tearDown(self):
#         self.user.delete()

#     def test_correct(self):
#         response = self.client.post('/login', {'username': 'test', 'password': '12test12'})
#         self.assertFalse(response.data[''])

#     def test_wrong_username(self):
#         response = self.client.post('/login/', {'username': 'wrong', 'password': '12test12'})
#         self.assertFalse(response.data[''])

#     def test_wrong_pssword(self):
#         response = self.client.post('/login/', {'username': 'test', 'password': 'wrong'})
#         self.assertFalse(response.data[''])


# class SignInViewTest(TestCase):


#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test',
#                                                          password='12test12',
#                                                          email='test@example.com')

#     def tearDown(self):
#         self.user.delete()


#     def test_call_view_load(self):
#         self.client.login(username='test', password='12test12')  # defined in fixture or with factory in setUp()
#         response = self.client.get('/login')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, '')

#     def test_call_view_fail_blank(self):
#         self.client.login(username='test', password='12test12')
#         response = self.client.post('/login', {}) # blank data dictionary
#         self.assertFormError(response, 'form', 'some_field', 'This field is required.')
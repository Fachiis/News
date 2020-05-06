from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageTest(SimpleTestCase):

    def test_homepage_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_homepage_view_url(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_homepage_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('home.html')


class SignupPageTest(TestCase):

    def setUp(self):
        self.new_user = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@gmail.com",
        )

        self.new_user2 = get_user_model().objects.create_user(
            username = "testuserobject2",
            email = "user@yahoo.com",
        )

    def test_signuppage_status_code(self):
        resp = self.client.get('/users/signup/')
        self.assertEqual(resp.status_code, 200)

    def test_signuppage_view_url(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)

    def test_signuppage_template(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('signup.html')

    def test_signup_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 2)
        self.assertEqual(get_user_model().objects.all()[0].username, self.new_user.username)
        self.assertEqual(get_user_model().objects.all()[1].username, self.new_user2.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.new_user.email)
        self.assertEqual(get_user_model().objects.all()[1].email, self.new_user2.email)
        
        







    
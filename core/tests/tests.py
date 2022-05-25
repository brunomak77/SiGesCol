from django.test import TestCase

class TestHomeView(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_has_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')
#
# class TestLoginView(TestCase):
#
#     def setUp(self):
#         self.resp = self.client.get('/login/')
#
#     def test_get(self):
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_has_template(self):
#         self.assertTemplateUsed(self.resp, 'login.html')
#
# class TestRegisterView(TestCase):
#
#     def setUp(self):
#         self.resp = self.client.get('/register/')
#
#     def test_get(self):
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_has_template(self):
#         self.assertTemplateUsed(self.resp, 'register.html')
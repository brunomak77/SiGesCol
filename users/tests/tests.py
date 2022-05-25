# from django.test import TestCase
#
# class TestLogoutView(TestCase):
#
#     def setUp(self):
#         self.resp = self.client.get('/users/logout/')
#
#     def test_get(self):
#         self.assertEqual(200, self.resp.status_code)
#     #
#     def test_has_template(self):
#         self.assertTemplateUsed(self.resp, 'logout.html')
#
# class TestProfileView(TestCase):
#     def setUp(self):
#         self.resp = self.client.get('/users/profile/')
#
#     def test_get(self):
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_has_template(self):
#         self.assertTemplateUsed(self.resp, 'profile.html')
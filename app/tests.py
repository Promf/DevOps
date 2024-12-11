from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

# Пример теста для модели (если у вас есть модель TestModel)
# class TestModelTest(TestCase):
#     def test_model_creation(self):
#         instance = TestModel.objects.create(name="Test Instance")
#         self.assertEqual(instance.name, "Test Instance")

# Пример теста для представления (view)
class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home')) # 'home' - имя вашего URL
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Welcome</h1>') # Проверяем наличие заголовка

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hi there!')
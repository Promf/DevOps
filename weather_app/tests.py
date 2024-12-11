from django.test import TestCase
from django.urls import reverse
from .models import TestModel

class TestModelTest(TestCase):
    def setUp(self):
        # Создаем тестовый объект перед каждым тестом
        self.test_model = TestModel.objects.create(name="Test Instance")

    def test_model_creation(self):
        # Проверяем, что объект создался корректно
        self.assertEqual(self.test_model.name, "Test Instance")

    def test_model_str_representation(self):
        # Проверяем строковое представление модели
        self.assertEqual(str(self.test_model), "Test Instance")

# Тесты для представлений (views)
class WeatherAppViewsTest(TestCase):
    def test_index_page_status_code(self):
        # Проверяем, что страница index возвращает код 200
        response = self.client.get(reverse('index'))  # 'index' - имя вашего URL из weather_app/urls.py
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_correct_template(self):
        # Проверяем, что страница index использует правильный шаблон
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'weather_app/index.html') # Замените, если у вас другой шаблон
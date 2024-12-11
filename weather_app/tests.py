from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse


class WeatherAppTests(TestCase):
    def test_index_url_exists(self):
        """
        Проверяем, что URL главной страницы доступен.
        """
        response = self.client.get(reverse('weather_app:index'))
        self.assertEqual(response.status_code, 200, "Страница index не доступна.")

    def test_index_uses_correct_template(self):
        """
        Проверяем, что представление index использует правильный шаблон.
        """
        response = self.client.get(reverse('weather_app:index'))
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_index_content(self):
   
        response = self.client.get(reverse('weather_app:index'))
        # Проверяем наличие базовых тегов
        self.assertContains(response, '<html lang="en">')  # Учитываем атрибут lang
        self.assertContains(response, '<body>')
        self.assertContains(response, '<title>What\'s the weather like?</title>')
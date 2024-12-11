from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('weather_app:index')) # 'weather_app:index',  app_name
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get(reverse('weather_app:index'))
        self.assertContains(response, "<h1>Weather App</h1>")  # Замените на ожидаемый HTML

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('weather_app:index'))
        self.assertNotContains(response, "<h1>Error Page</h1>") # Замените на некорректный HTML
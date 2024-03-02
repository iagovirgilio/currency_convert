from django.test import TestCase, Client
from django.urls import reverse
from .views import get_exchange_rate

class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('convert:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'convert/index.html')

    def test_convert_currency(self):
        # Teste para conversão de moeda bem-sucedida
        response = self.client.get('/api/convert/?from=USD&to=BRL&amount=100')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('converted_amount', data)

        # Teste para conversão de moeda com taxa de câmbio não disponível
        response = self.client.get('/api/convert/?from=USD&to=XYZ&amount=100')
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_get_exchange_rate(self):
        # Teste para obter taxa de câmbio bem-sucedida
        rate = get_exchange_rate('USD', 'BRL')
        self.assertIsNotNone(rate)

        # Teste para obter taxa de câmbio com moeda inválida
        rate = get_exchange_rate('XYZ', 'BRL')
        self.assertIsNone(rate)

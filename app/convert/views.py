from django.shortcuts import render
from django.http import JsonResponse
import requests


def index(request):
    """Renderiza a página inicial."""
    return render(request, 'convert/index.html')


def convert_currency(request):
    """Converte uma quantia de uma moeda para outra."""
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = float(request.GET.get('amount'))

    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return JsonResponse({'error': 'Taxa de câmbio não disponível'}, status=400)

    converted_amount = round(amount * rate, 2)
    return JsonResponse({'converted_amount': converted_amount})


def get_exchange_rate(from_currency, to_currency):
    """Obtém a taxa de câmbio de uma moeda para outra."""
    base_url = "https://api.exchangerate-api.com/v4/latest/"
    url = f"{base_url}/{from_currency}"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    rates = data.get("rates")
    if not rates or to_currency not in rates:
        return None
    
    return rates[to_currency]

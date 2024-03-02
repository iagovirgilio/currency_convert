from django.shortcuts import render
from django.http import JsonResponse
import requests
from .utils import format_brazilian_currency


def index(request):
    """Renderiza a página inicial."""
    return render(request, 'convert/index.html')


def convert_currency(request):
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = float(request.GET.get('amount'))

    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return JsonResponse({'error': 'Taxa de câmbio não disponível'}, status=400)

    converted_amount = round(amount * rate, 4)

    formatted_amount = format_brazilian_currency(converted_amount, 4)
    
    return JsonResponse({'converted_amount': formatted_amount})


def get_exchange_rate(from_currency, to_currency):
    base_url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': from_currency, 'vs_currencies': to_currency}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200:
        return None

    rates = data.get(from_currency.lower())
    if not rates or to_currency.lower() not in rates:
        return None
    
    return rates[to_currency.lower()]

from django.urls import path
from convert.views import index, convert_currency

app_name = 'convert'

urlpatterns = [
    path('', index, name='index'),
    path('api/convert/', convert_currency, name='convert_currency'),
]

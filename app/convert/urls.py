from django.urls import path
from convert.views import index

app_name = 'convert'

urlpatterns = [
    path('', index, name='index'),
]

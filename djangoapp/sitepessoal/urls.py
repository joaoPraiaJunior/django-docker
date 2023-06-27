
from django.urls import path
from sitepessoal.views import index

app_name = 'sitepessoal'

urlpatterns = [
    path('',  index, name='index'),
]


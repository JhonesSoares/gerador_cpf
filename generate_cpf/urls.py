from django.urls import path

from generate_cpf import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]    
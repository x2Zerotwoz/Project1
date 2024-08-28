from django.urls import path
from . import views

urlpatterns = [
    path('abount/', views.abount, name='abount'),
]
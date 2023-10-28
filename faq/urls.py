from django.urls import path
from . import views

urlpatterns = [
    path('', views.FAQList, name='FAQList'),
    path('add/', views.add_faq, name='add_faq'),
]

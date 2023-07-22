from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_short_url, name='create_short_url'),  # Redirect to create_short_url view
    path('create/', views.create_short_url, name='create_short_url'),
    path('<str:short_id>/', views.redirect_to_original, name='redirect_to_original'),
]


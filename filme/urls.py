# url, view, template
from django.urls import path, include

from .views import Homepage, Homefilmes


# 🔗 Rotas principais do site
urlpatterns = [
    path('', Homepage.as_view()),  # inclui as rotas do app "filme"
    path('filmes', Homefilmes.as_view()),
]

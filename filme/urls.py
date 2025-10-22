# url, view, template
from django.urls import path, include

from .views import homepage, homefilmes


# 🔗 Rotas principais do site
urlpatterns = [
    path('', homepage),  # inclui as rotas do app "filme"
    path('filmes', homefilmes),
]

# url, view, template
from django.urls import path, include

from .views import homepage


# 🔗 Rotas principais do site
urlpatterns = [
    path('', homepage),  # inclui as rotas do app "filme"
]

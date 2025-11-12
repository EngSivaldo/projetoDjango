# url, view, template
from django.urls import path, include

from .views import Homepage, Homefilmes,Detalhesfilme,Pesquisafilme
from . import views

app_name = 'filme'
# nome do app(filme)

# 🔗 Rotas principais do site
urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),  # inclui as rotas do app "filme"
    path('filmes', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('episodio/<int:pk>/', views.EpisodioDetailView.as_view(), name='episodio_detalhe'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme')

]

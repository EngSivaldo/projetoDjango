# url, view, template
from django.urls import path, include

from .views import Homepage, Homefilmes,Detalhesfilme,Pesquisafilme
from . import views
from django.contrib.auth import views as auth_view#para criar url de login padrao

app_name = 'filme'
# nome do app(filme)

# 🔗 Rotas principais do site que estao nao views.py
urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),  # inclui as rotas do app "filme"
    path('filmes', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('episodio/<int:pk>/', views.EpisodioDetailView.as_view(), name='episodio_detalhe'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    #está usando a View padrão do Django LoginView.as_asview().
    path('login/',auth_view.LoginView.as_view(template_name='login.html') , name='login'),
    #está usando a View padrão do Django LogoutView.as_asview().
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html') , name='logout'),


]

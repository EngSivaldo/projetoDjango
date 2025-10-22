from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from filme.models import Filme


class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
   # obeject_list -> lista de itens do modelo


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
       # obeject -> item do modelo



# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")








# çriar uma nova views  (url- view - html- models)
# def homefilmes(request):
#     context = {}
#
#     lista_filmes = Filme.objects.all()  # chamar esta variavel listafilmes no homefilmes.html
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

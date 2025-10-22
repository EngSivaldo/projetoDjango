from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from filme.models import Filme


# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")


class Homepage(TemplateView):
    template_name = "homepage.html"



# çriar uma nova views  (url- view - html- models)
# def homefilmes(request):
#     context = {}
#
#     lista_filmes = Filme.objects.all()  # chamar esta variavel listafilmes no homefilmes.html
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme

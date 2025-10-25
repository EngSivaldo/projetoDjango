from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from filme.models import Filme, Episodio


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
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtra a minha tabela de filmes, pegar filmes por categoria
        #self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"]= filmes_relacionados
        return context


# ✅ Nova view para abrir o episódio em tela cheia
class EpisodioDetailView(DetailView):
    model = Episodio
    template_name = "episodio_detalhe.html"

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

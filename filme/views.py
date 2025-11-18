from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from filme.models import Filme, Episodio
from django.contrib.auth.mixins import LoginRequiredMixin#bloquear usu nao logado
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args,**kwargs):
        if request.user.is_authenticated:#se usuario autenticado
            return redirect('filme:homefilmes')#redirec para homefilmes
        else:
            return super().get(request, *args, **kwargs)#redirec para homepage

#bloquear usu nao logado(LoginRequiredMixin),cofig, no settings(redirecionaRr
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
   # obeject_list -> lista de itens do modelo


class Detalhesfilme(LoginRequiredMixin,DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        # 1. Obter o objeto filme
        filme = self.get_object()

        # 2. Incrementar visualizações
        filme.visualizacoes += 1
        filme.save()

        # ✅ 3. Lógica para adicionar o filme na lista 'filmes_vistos' do usuário
        if request.user.is_authenticated:
            # O método .add() garante que só será adicionado se o filme ainda não estiver na lista.
            request.user.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs) # redireciona para url final

    # ... (o restante da sua get_context_data permanece inalterado)


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtra a minha tabela de filmes, pegar filmes por categoria
        #self.get_object()
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"]= filmes_relacionados
        return context


# ✅ Nova view para abrir o episódio em tela cheia
class EpisodioDetailView(LoginRequiredMixin,DetailView):
    model = Episodio
    template_name = "episodio_detalhe.html"



class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termopesquisa = self.request.GET.get('query')
        if termopesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termopesquisa)
            return object_list
        else:
            return None



class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"


class Criarconta(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "criarconta.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if not form.is_valid():
            # Dicionário para substituir mensagens padrões
            mensagens_custom = {
                "This password is too short. It must contain at least 8 characters.":
                    "A senha precisa ter no mínimo 8 caracteres.",
                "This password is too common.":
                    "A senha escolhida é muito comum. Tente uma mais forte.",
                "This password is entirely numeric.":
                    "A senha não pode ser apenas números.",
            }

            # Substitui mensagens
            for field in form.errors:
                novas_msgs = []
                for erro in form.errors[field]:
                    novas_msgs.append(mensagens_custom.get(erro, erro))
                form.errors[field] = novas_msgs

        if form.is_valid():
            form.save()
            return redirect("filme:login")

        return render(request, "criarconta.html", {"form": form})









# çriar uma nova views  (url- view - html- models)
# def homefilmes(request):
#     context = {}
#
#     lista_filmes = Filme.objects.all()  # chamar esta variavel listafilmes no homefilmes.html
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

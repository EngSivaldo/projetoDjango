from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from filme.models import Filme, Episodio, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin#bloquear usu nao logado
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CriarContaForm, FormHomepage
from django.urls import reverse_lazy


from django.contrib.auth.mixins import UserPassesTestMixin

class Homepage(UserPassesTestMixin, FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('filme:homefilmes')

    def get_success_url(self):
        email = self.request.POST.get("email")
        if Usuario.objects.filter(email=email).exists():
            return reverse_lazy('filme:login')
        return reverse_lazy('filme:criarconta')



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



class Paginaperfil(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "editarperfil.html")

    def post(self, request):

        user = request.user

        # Recebe dados do formulário
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.save()

        # Atualiza foto
        perfil = user.perfil  # seu OneToOneField
        foto = request.FILES.get("foto")

        if foto:
            perfil.foto = foto
            perfil.save()

        return redirect("filme:homepage")


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("filme:login")

    mensagens_custom = {
        "This password is too short. It must contain at least 8 characters.":
            "A senha precisa ter no mínimo 8 caracteres.",
        "This password is too common.":
            "A senha escolhida é muito comum. Tente uma mais forte.",
        "This password is entirely numeric.":
            "A senha não pode ser apenas números.",
    }

    def form_invalid(self, form):
        # Substitui mensagens padrões pelas mensagens customizadas
        for field in form.errors:
            novas_msgs = []
            for erro in form.errors[field]:
                novas_msgs.append(self.mensagens_custom.get(erro, erro))
            form.errors[field] = novas_msgs

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)





class EditarPerfilView(LoginRequiredMixin, View):
    template_name = "editarperfil.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = request.user

        # Atualizar dados básicos
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.save()

        # Atualizar foto do perfil (se enviada)
        if "foto" in request.FILES:
            user.perfil.foto = request.FILES["foto"]
            user.perfil.save()

        return redirect("filme:editarperfil")  # ← FICA NA MESMA PÁGINA





# çriar uma nova views  (url- view - html- models)
# def homefilmes(request):
#     context = {}
#
#     lista_filmes = Filme.objects.all()  # chamar esta variavel listafilmes no homefilmes.html
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

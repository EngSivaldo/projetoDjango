from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    filme_destaque = lista_filmes[0]
    return {"lista_filmes_recentes": lista_filmes, 'filme_destaque':filme_destaque }


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {'lista_filmes_emalta': lista_filmes}



# def filme_destaque(request):
#     filme = Filme.objects.all().order_by('-data_criacao')[0]
#     return {"filme_destaque":filme}

# apos criar os novos contextos, para conextar ao resto do projeto,
# registra em settings.py em TEMPLATES/OPTIONS

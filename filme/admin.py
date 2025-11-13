from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin


# 1. Subclasse do UserAdmin para customizar o formulário
class CustomUserAdmin(UserAdmin):
    # Cria uma tupla de fieldsets. O fieldsets padrão do UserAdmin
    # é herdado e seu campo é adicionado.
    fieldsets = UserAdmin.fieldsets + (
        ('Histórico', {'fields': ('filmes_vistos',)}),
    )

    # Opcional: Para que o campo "Histórico" apareça no painel de detalhes do usuário
    # em vez de ser editável diretamente na tela de edição.
    # Você também pode personalizar 'add_fieldsets' se quiser que apareça ao criar.


# 2. Registra os modelos
admin.site.register(Filme)
admin.site.register(Episodio)

# 3. Registra o modelo Usuario usando a classe customizada
admin.site.register(Usuario, CustomUserAdmin)

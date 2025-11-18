from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CriarContaForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "password1", "password2")



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # deixa os campos no estilo do seu login
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full p-2 rounded bg-gray-700 text-white"
            })

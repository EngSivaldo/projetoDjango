from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms



class FormHomepage(forms.Form):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Digite seu e-mail"
        })
    )

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ("username",'email', "password1", "password2")



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

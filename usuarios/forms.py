from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    grupo = forms.ModelChoiceField(queryset=Group.objects.filter(name__in=["Condomino", "Porteiros"]), required=True)

    class Meta:
        model = User
        fields = ['username', 'grupo', 'email', 'password1', 'password2']
from django import forms
from enderecos.models import Enderecos

class Cadastro(forms.ModelForm):
    class Meta:
        model = Enderecos
        fields = "__all__"
        widgets = {
            'cep': forms.TextInput(attrs={'onBlur': "pesquisacep(this.value);"})
        }

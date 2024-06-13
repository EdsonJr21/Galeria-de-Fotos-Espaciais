from django import forms

class loginForms(forms.Form):
    nome_login = forms.CharField(
        label= "nome de login",
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha = forms.CharField(
        label= "senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= "Nome de cadastro",
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label= "Email",
        required= True,
        max_length= 100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Joaosilva@xpto.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label= "Senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label= "Confirme sua senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
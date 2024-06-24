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
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é permitido incluir espaços no campo Nome de cadastro")
            else:
                return nome          
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas não são iguais")
            else:
                return senha_2
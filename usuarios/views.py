from django.shortcuts import render, redirect

from usuarios.forms import loginForms, cadastroForms

def login(request):
    form = loginForms()
    return render(request, "usuarios/login.html", {"form": form})
def cadastro(request):
    form = cadastroForms()

    if request.method == 'POST':
        form = cadastroForms(request.POST)
        
        if form["senha_1"].value() != form["senha_2"].value():
            return redirect('cadastro')
        


    return render(request, "usuarios/cadastro.html", {"form": form})

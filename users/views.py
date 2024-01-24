from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method != 'POST':
        #exibe o formulário de registro em branco
        form = UserCreationForm()
    else:
        # processa o formulário enviado
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # faz o login do usuário e o redireciona para a página inical
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)
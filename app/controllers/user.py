from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def create(request):
    return render(request, 'user/create.html')

def do_create(request, **kw):
    params = request.POST
    try:
        user = User.objects.create_user(params['username'],
                                                        params['email'],
                                                        params['password'])
        user.save()
    except KeyError:
        return HttpResponse("Todos os campos são necessários")

    return redirect('/equipamento')

def edit(request, id):
    pass

def do_edit(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def login(request):
    if request.user.is_authenticated():
        return redirect('/equipamento')

    return render(request, 'user/login.html')

def do_login(request):
    params = request.POST

    try:
        user = auth.authenticate(username=params['username'], password=params['password'])
    except KeyError:
        return HttpResponse("É necessário username e senha pra fazer login")

    if user:
        auth.login(request, user)
        return redirect('/qrcode')
    else:
        return HttpResponse("Usuário não encontrado")


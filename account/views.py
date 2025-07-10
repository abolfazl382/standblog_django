from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    context = {'errors' : []}

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if password != confirm_password:
            context['errors'].append("Passwords don't match")
            return render(request, 'account/register.html', context = context)

        # if User.objects.get(username=username):
        #     context['errors'].append("This username is already registered")
        #     return render(request, 'account/register.html', context=context)

        user = User.objects.create_user(username=username, password=password, email=email) # .create() didn't work
        login(request, user)
        return redirect('/')

    return render(request, 'account/register.html')

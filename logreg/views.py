from django.shortcuts import render

def login(request):
    return render(request, 'templates/logreg/login.html', {})

def register(request):
    return render(request, 'logreg/register.html', {})

def dashboard(request):
    return render(request, 'logreg/dashboard.html', {})

def logout(request):
    return render(request, 'logreg/logout.html', {})



from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def logout(request):
    return redirect("main:login")


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:login")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request, template_name="main/register.html", context={"form": form})

    form = UserCreationForm
    return render(request=request, template_name="main/register.html", context={"form": form})


def result(request):
    return render(request=request, template_name="main/result.html", context={})


def pay(request):
    return render(request=request, template_name="main/request.html", context={})


def reval(request):
    return render(request=request, template_name="main/reval.html", context={})

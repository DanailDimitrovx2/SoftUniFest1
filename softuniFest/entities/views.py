from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import News, User


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('home')
        else:
            {'form': form}
    else:
        form=RegistrationForm()
        return render(request, 'users/register.html', {'form': form})

def home(request):
    news=News.objects.all()
    users=User.objects.all()
    return render(request, 'users/home.html', {'news': news,
                                               'users':users})

def user_profile(request, user_id):
    user=User.objects.get(pk=user_id)
    return render(request, 'users/user_profile.html', {'user': user})







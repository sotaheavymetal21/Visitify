from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserCreateForm


@login_required
def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request) # ログアウト処理を行うため、logout()関数を呼び出す
    return redirect('home') # ログアウト後にリダイレクトするため、redirect()関数を呼び出す

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

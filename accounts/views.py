from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreateForm, UserProfileForm


def home(request):
    return render(request, "home.html")

@login_required
def user_logout(request):
    logout(request) # ログアウト処理を行うため、logout()関数を呼び出す
    return redirect("home") # ログアウト後にリダイレクトするため、redirect()関数を呼び出す



class CustomLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("profile")


from django.contrib.auth.hashers import make_password

from django.db.utils import IntegrityError

def signup(request):
    if request.method == "POST":
        user_form = UserCreateForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Userモデルの登録
            user = user_form.save(commit=False)
            # パスワードをハッシュ化する
            user.password = make_password(user_form.cleaned_data.get('password1'))
            try:
                user.save()
            except IntegrityError:
                # ユーザー名またはメールアドレスが既に存在している場合、エラーを表示してフォームを再表示する
                user_form.add_error(None, "ユーザー名またはメールアドレスが既に存在しています")
                return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})
            # UserProfileモデルの登録
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # ログイン処理
            raw_password = user_form.cleaned_data.get('password1')
            # ユーザーを認証する
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        user_form = UserCreateForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})





@login_required
def profile(request):
    user_profile = request.user
    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)

@login_required
def profile_edit(request):
    user_profile = User.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    context = {'form': form}
    return render(request, 'profile_edit.html', context)
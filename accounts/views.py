from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserCreateForm

def user_login(request):
    if request.method == 'POST':  # POSTリクエストの場合、フォームが送信されたと見なされます。
        form = LoginForm(request.POST)  # LoginFormから入力されたデータを取得します。
        if form.is_valid():  # フォームが有効であるかどうかを確認します。
            username = form.cleaned_data['username']  # フォームからユーザー名を取得します。
            password = form.cleaned_data['password']  # フォームからパスワードを取得します。
            user = authenticate(request, username=username, password=password)  # ユーザーが認証されるかどうかを確認します。
            if user is not None:  # ユーザーが認証された場合、ログインします。
                login(request, user)
                return redirect('spot_list')  # ログイン後にリダイレクトする場所を指定します。
            else:  # 認証に失敗した場合、エラーメッセージをフォームに追加します。
                form.add_error(None, 'ユーザー名またはパスワードが正しくありません。')
    else:  # GETリクエストの場合、空のフォームを表示します。
        form = LoginForm()
    return render(request, 'login.html', {'form': form})  # ログインページを表示します。



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

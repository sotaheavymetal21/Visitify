from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('spot_list')  # 観光スポット一覧ページにリダイレクト
            else:
                form.add_error(None, 'ユーザー名またはパスワードが正しくありません。')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({'token': user.auth_token.key})
        else:
            return JsonResponse({'error': 'ユーザー名またはパスワードが正しくありません。'}, status=400)
    else:
        return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=400)

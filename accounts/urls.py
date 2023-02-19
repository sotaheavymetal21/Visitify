# path関数をインポート
from django.urls import path
from .views import login_view, login_api


urlpatterns = [
  path("login/", login_view, name="login"),
  path('api/login/', login_api, name='login_api'),
]

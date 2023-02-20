# path関数をインポート
from django.urls import path
from .views import login_view, signup


urlpatterns = [
  path("login/", login_view, name="login"),
  path("signup/", signup, name="signup"),
]

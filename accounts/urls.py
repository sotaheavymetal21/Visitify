# path関数をインポート
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import user_logout, signup, home


urlpatterns = [
  path('', home, name='home'),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', user_logout, name='logout'),
  path("signup/", signup, name="signup"),
  path("profile/", views.profile_view, name="profile"),
  path("profile/edit/", views.profile_edit_view, name="profile_edit")
]
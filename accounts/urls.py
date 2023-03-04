# path関数をインポート
from django.urls import path
from .views import CustomLoginView, user_logout, signup, home, profile, profile_edit

urlpatterns = [
  path('', home, name='home'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', user_logout, name='logout'),
  path("signup/", signup, name="signup"),
  path("profile/", profile, name="profile"),
  path("profile/edit/", profile_edit, name="profile_edit")
]
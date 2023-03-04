from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label="お名前(名)")
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.', label="お名前（姓）")
    email = forms.EmailField(required=True, help_text='必須です。', label='メールアドレス')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image', 'introduction', 'website', 'occupation', 'skills', 'free_text']
        labels = {"profile_image": "プロフィール画像","introduction": "自己紹介","website": "個人のウェブサイト","occupation": "職業","skills": "スキル","free_text": "自由記入欄",}

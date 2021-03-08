from django import forms
from django.contrib.auth.models import User
from profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('last_name', 'first_name', 'patronymic', 'avatar', 'information')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.clear_checkbox_label = 'Очистить'
        self.fields['avatar'].widget.initial_text = "(текущий)"
        self.fields['avatar'].widget.input_text = "Новый"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

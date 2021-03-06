from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from fashion_store.web.models import Profile


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
    )
    last_name = forms.CharField(
        max_length=30,
    )
    picture = forms.URLField(
        max_length=300,
    )
    description = forms.CharField(
        widget=forms.Textarea,
    )
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            description=self.cleaned_data['description'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }

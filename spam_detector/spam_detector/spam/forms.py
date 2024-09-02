from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import NewUser

class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if NewUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

class NewUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = NewUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(NewUserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs.update({'autofocus': True})

class SpamNumberSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False)
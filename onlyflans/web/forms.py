from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100, required=True)  # Campo para el nombre

    class Meta:
        model = User
        fields = ['username', 'name', 'password']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Establece la contraseña
        if commit:
            user.save()
        return user
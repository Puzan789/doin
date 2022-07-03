
from django import forms
class blogform(forms.Form):
    title = forms.CharField(label='title')
    email=forms.EmailField(label='email')
    password=forms.CharField(widget=forms.PasswordInput(),label='password')

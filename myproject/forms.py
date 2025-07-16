

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    country = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

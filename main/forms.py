from django import forms

class emailForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='name', max_length=100)
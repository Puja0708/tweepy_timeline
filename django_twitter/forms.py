from django import forms

class ContactForm(forms.Form):
    q = forms.CharField(label="twitter handle")
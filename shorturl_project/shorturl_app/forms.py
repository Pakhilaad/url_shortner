from django import forms

class ShortURLForm(forms.Form):
    original_url = forms.URLField(label='Enter your URL:', max_length=2000)

from django import forms

class JmxUploadForm(forms.Form):
    name = forms.CharField(
        label='Give it a name', max_length=50, 
        widget=forms.TextInput(
            attrs={'placeholder': 'Script Name', 'autocomplete': 'off'}))
    jmxfile = forms.FileField(
        label='Upload jmx') # widget=forms.FileInput(attrs={})


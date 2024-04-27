from django import forms
class CDRUploadForm(forms.Form):
    cdr_file = forms.FileField()

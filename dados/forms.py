from django import forms

class CSVUploadForm(forms.Form):
    arquivo = forms.FileField()

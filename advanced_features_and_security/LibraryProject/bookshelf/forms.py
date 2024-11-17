from django import forms

class ExampleForm(forms.Form):
    book_name = forms.CharField(max_length=100, required=True)
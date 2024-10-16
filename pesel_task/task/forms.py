from django import forms


class PeselForm(forms.Form):
    pesel = forms.IntegerField(required=True)

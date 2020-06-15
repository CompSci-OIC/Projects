from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label = 'smth', max_length = 100)

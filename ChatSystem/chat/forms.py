from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label = '', max_length = 100, widget = forms.TextInput(attrs = {
        'type':"text",
        'placeholder':"Enter name here",
        'id':"nameForm"}))

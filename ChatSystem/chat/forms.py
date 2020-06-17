from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label = '', max_length = 100, widget = forms.TextInput(attrs = {
        'type':"text",
        'placeholder':"Enter name here",
        'id':"nameForm",
        'novalidate': "True"
        }))

class GroupForm(forms.Form):
    group_name = forms.CharField(label ='',max_length = 50, widget = forms.TextInput(attrs ={
        'type':"text",
        'placeholder': "Enter Group Name",
        'id':'groupsetupForm'}))



class JoinGroupForm(forms.Form):
    group_id = forms.CharField(label ='',max_length = 50, widget = forms.TextInput(attrs ={
        'type':"text",
        'placeholder': "Enter Group ID",
        'id':'groupsetupForm'}))

from django import forms

class HomePage(forms.Form):
    choice = forms.ChoiceField(choices=('Create_account','User Login','Admin Login','Guest',))
    
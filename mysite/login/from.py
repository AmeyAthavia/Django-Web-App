from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=50)
    uname = forms.CharField(label='Username',max_length=20)
    cpass = forms.PasswordInput()
    gender = forms.ChoiceField(choices=('male','female','other'))
    mail = forms.EmailField()
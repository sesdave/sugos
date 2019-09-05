from allauth.account.forms import SignupForm
from django import forms

ACCOUNT_CHOICE=[
    ('business','Business'),
    ('marketer','Marketer'),
    ('individual','Individual'),
]

class CustomSignupForm(SignupForm):
    first_name = forms.ChoiceField(choices=ACCOUNT_CHOICE)
    #account_type = forms.IntegerField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user
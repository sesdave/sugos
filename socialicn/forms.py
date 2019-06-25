from allauth.account.forms import SignupForm
from django import forms

ACCOUNT_CHOICE=[
    ('business','Business'),
    ('marketer','Marketer'),
    ('individual','Individual'),
]

class CustomSignupForm(SignupForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICE)
    #account_type = forms.IntegerField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['account_type']
        user.save()
        return user
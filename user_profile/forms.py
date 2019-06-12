from user_profile.models import UserProfile
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'rc_number', 'company_name', 'website')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })




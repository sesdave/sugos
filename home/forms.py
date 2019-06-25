from django import forms
from home.models import Post
from home.models import UserMessage


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post','videofile')

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = UserMessage
        fields = ('message',)
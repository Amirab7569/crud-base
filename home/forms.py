from django import forms
from .models import Post

class CreatePost(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    body = forms.CharField()
    created=forms.DateTimeField()


class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
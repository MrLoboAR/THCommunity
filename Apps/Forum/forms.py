from django import forms
from .models import Post

class Add_Thread_F(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
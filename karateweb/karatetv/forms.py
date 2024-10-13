from django import forms

from .models import PostSE, PostTV

class PostFormSE(forms.ModelForm):

    class Meta:
        model = PostSE
        fields = ('title', 'text', 'image')

class PostFormTV(forms.ModelForm):
    
    class Meta:
        model = PostTV
        fields = ('title', 'text', 'image')

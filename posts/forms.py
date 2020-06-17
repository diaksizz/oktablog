from django.forms import ModelForm 
from django import forms
from .models import Category,Posts,Comment



class PostForm(ModelForm):

    class Meta:
        model = Posts 
        fields =['author','category','title','description','slug','featured_image','published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
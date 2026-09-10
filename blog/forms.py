from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:model=User;fields=('username','email','password1','password2')
class PostForm(forms.ModelForm):
    tags=forms.CharField(required=False,help_text='Comma-separated tags')
    class Meta:model=Post;fields=('title','excerpt','content','tags')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if self.instance.pk:self.fields['tags'].initial=', '.join(self.instance.tags.values_list('name',flat=True))
    def save(self,commit=True):
        post=super().save(commit=commit)
        if commit:
            from .models import Tag
            post.tags.clear()
            for name in [x.strip() for x in self.cleaned_data['tags'].split(',') if x.strip()]:post.tags.add(Tag.objects.get_or_create(name=name)[0])
        return post
class CommentForm(forms.ModelForm):
    class Meta:model=Comment;fields=('body',);widgets={'body':forms.Textarea(attrs={'rows':4,'placeholder':'Write a thoughtful comment...'})}

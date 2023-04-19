from django import forms
from blogs.models import Blog, Post


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blogs title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something down here...'}),
        }


class CreatePostForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something down here...'}),
        }



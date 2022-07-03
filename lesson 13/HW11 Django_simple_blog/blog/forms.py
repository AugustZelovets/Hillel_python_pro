from django import forms

from .models import *


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Post
        fields = ['title', 'category', 'text', ]
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

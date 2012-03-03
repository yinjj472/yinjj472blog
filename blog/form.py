from django import forms
from blog.models import Article, Category

__author__ = 'Administrator'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
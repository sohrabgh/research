from django import forms
from blog.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title',)
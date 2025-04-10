from django import forms

# Book を使うためにインポート
from .models import Book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "author", "creator"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "author", "creator"]
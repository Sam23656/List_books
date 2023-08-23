from django import forms
from Books.models import Book, Author, Genre


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["Name", "Slug", "Year", "Author", "Genre", "Rating"]
        widgets = {
            "Rating": forms.NumberInput(attrs={'min': 0, 'max': 10})
        }


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

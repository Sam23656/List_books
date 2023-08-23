from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from Books.forms import *
from Books.models import Book, Author, Genre


# Create your views here.

def show_index_page(request):
    context = {"BookCount": Book.objects.count(),
               "AuthorCount": Author.objects.count(),
               "GenreCount": Genre.objects.count()}
    return render(request, 'index.html', context=context)


class ShowBookList(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "Books"


class ShowBookDetail(DetailView):
    model = Book
    template_name = "book_detail.html"
    slug_field = "Slug"
    slug_url_kwarg = "slug_param"
    context_object_name = "Book"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.update_watch_count()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ShowBookDelete(DeleteView):
    model = Book
    template_name = "book_delete.html"
    slug_field = "Slug"
    slug_url_kwarg = "slug_param"
    success_url = reverse_lazy("book_list")
    context_object_name = "Book"


class ShowBookUpdate(UpdateView):
    model = Book
    template_name = "book_update.html"
    form_class = AddBookForm
    slug_field = "Slug"
    slug_url_kwarg = "slug_param"
    success_url = reverse_lazy("book_list")
    context_object_name = "Book"


def show_book_add(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_list')
    else:
        form = AddBookForm()

    author_form = AddAuthorForm(request.POST or None)
    if request.method == 'POST' and author_form.is_valid():
        author_form.save()
        return redirect('book_list')

    genre_form = AddGenreForm(request.POST or None)
    if request.method == 'POST' and genre_form.is_valid():
        genre_form.save()
        return redirect('book_list')

    context = {
        'form': form,
        'form2': author_form,
        'form3': genre_form
    }
    return render(request, 'book_add.html', context)

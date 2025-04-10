# test_app/views.py
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Book を使うためにインポート
from .models import Book 
from .forms import BookForm

from django.urls import reverse, reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = "test_app/book_list.html"
    context_object_name = "books"

class AddNewBookView(CreateView):
    model = Book
    template_name = "test_app/add_new_book.html"
    form_class = BookForm

    def get_success_url(self):
        # Book一覧に遷移する
        return reverse_lazy('book_list')
    
class UpdatebookView(UpdateView):
    model = Book
    template_name = "test_app/update_book.html"
    form_class = BookForm

    def get_success_url(self):
        # Book一覧に遷移する
        return reverse_lazy('book_list')
    
class DeleteBookView(DeleteView):
    model = Book
    template_name = "test_app/delete_book.html"

    def get_success_url(self):
        # Book一覧に遷移する
        return reverse_lazy('book_list')

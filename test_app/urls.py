from django.urls import path
from .views import *
  
urlpatterns = [
    # /にアクセスした時、BookListViewを呼び出す
    path("", BookListView.as_view(), name="book_list"),
    path("add_new_book", AddNewBookView.as_view(), name="add_book"),
    path("update_book/<int:pk>", UpdatebookView.as_view(), name="update_book"),
    path("delete_book/<int:pk>", DeleteBookView.as_view(), name="delete_book"),
]
"""
URL configuration for List_books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Books.views import show_index_page, ShowBookList, ShowBookDetail, ShowBookDelete, ShowBookUpdate, show_book_add

urlpatterns = [
    path('', show_index_page, name='index'),
    path('book_list/', ShowBookList.as_view(), name='book_list'),
    path('book_detail/<slug_param>/', ShowBookDetail.as_view(), name='book_detail'),
    path('book_delete/<slug_param>/', ShowBookDelete.as_view(), name='book_delete'),
    path('book_update/<slug_param>/', ShowBookUpdate.as_view(), name='book_update'),
    path('add_book/', show_book_add, name='book_add'),
    path('admin/', admin.site.urls),
]

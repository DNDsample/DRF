from django.contrib import admin
from .models import Book
@ admin.register(Book)
class Book_admin(admin.ModelAdmin):
    list_display = ['id','author','publication_date']


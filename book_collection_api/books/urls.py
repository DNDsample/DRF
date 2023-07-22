from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView, BookPartialUpdateView,schema_view

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('books/<int:pk>/partial/', BookPartialUpdateView.as_view(), name='book-partial-update'),
    # path('swagger/', schema_view, name ='get-swagger-view' )

]

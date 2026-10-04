from django.urls import path
from .views import author_view, author_entry

urlpatterns = [
    path("display-authors/", author_view, name="display_authors"),
    path("create-author/", author_entry, name="create_author"),
]
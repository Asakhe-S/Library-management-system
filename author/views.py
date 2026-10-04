from django.shortcuts import render, redirect
from .models import Author
from .forms import CreateAuthorEntry

# Create your views here.

def author_view(request):
    all_author = Author.objects.all().order_by("id")
    return render(
        request,
        "author/display_author.html",
        {"display_authors": all_author},
    )
    
def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")
    else:
        author_form = CreateAuthorEntry()
        
    context = {"create_form": author_form}
    return render(request, "author/create_author.html", context)

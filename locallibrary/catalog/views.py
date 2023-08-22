from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
from django.shortcuts import get_object_or_404
class BookDetailView(generic.DetailView):
    model = Book

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)   
    return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

from django.shortcuts import get_object_or_404
class AuthorDetailView(generic.DetailView):
    model = Author

def author_detail_view(request, primary_key):
    author = get_object_or_404(Author, pk=primary_key)   
    return render(request, 'catalog/author_detail.html', context={'author': author})

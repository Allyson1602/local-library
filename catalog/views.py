from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(self, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(self, 'catalog/author_detail.html', context={'author': author})


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10  # 2
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.all()


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(self, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(self, 'catalog/book_detail.html', context={'book': book})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10  # 2
    context_object_name = 'book_list'   # your own name for the list as a template variable
    # template_name = 'catalog/book_list.html'  # Specify your own template name/location

    # queryset = Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
    def get_queryset(self):
        return Book.objects.all()

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre = Genre.objects.all().count()

    # Books with word 'Mar'
    num_books_with_mar = Book.objects.filter(title__contains='Mar').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_books_with_mar': num_books_with_mar,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


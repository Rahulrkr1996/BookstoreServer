from django.shortcuts import render
import requests
from .models import Book

GOOGLE_BOOKS_URI_BASE_STRING = "https://www.googleapis.com/books/v1/volumes?q="
SEARCHBAR_NAME = "searchbar"


def view_inventory(request):
    context = {
        'books': Book.objects.order_by('-count')
    }
    return render(request, 'inventory/view.html', context)


def search_inventory(request):
    retrieved_books = []
    google_books = get_books_from_google(request)
    if len(google_books) > 0:
        for book in google_books:
            # Get id from http response
            current_id = book.get('id', None)
            print("Retrieved Id From response : " + str(current_id))
            try:
                # no-error = search element exists in DB ,get values
                db_item = Book.objects.filter(google_book_id=current_id).first()
                if db_item is not None:
                    print("Retrieved Id From DB : " + str(db_item))
                    item = {
                        'title': db_item.title,
                        'authors': db_item.authors,
                        'image': db_item.image,
                        'desc': db_item.desc,
                        'count': db_item.count
                    }
                    retrieved_books.append(item)
                    print("Got value from DB ")
                    print(db_item)
                else:
                    retrieved_books.append(create_new_book_from_data(book))
            except Book.DoesNotExist:  # search element does not exists in DB ,initialize new
                # getting values form http response
                retrieved_books.append(create_new_book_from_data(book))

        # retrieved_books.sort(key=lambda entry: entry['count'], reverse=True)
        print("retrieved books : "+str(retrieved_books))
    context = {
        'books': retrieved_books
    }
    return render(request, 'inventory/view.html', context)


def get_books_from_google(request):
    if request.method == "GET":
        print(request.GET.keys())
        books_url = GOOGLE_BOOKS_URI_BASE_STRING
        search_text = request.GET.get('search_input', None)
        print("Got value from search bar : " + str(search_text))
        if search_text is not None:
            inp_list = search_text.split()

            for keyword in inp_list:
                books_url += keyword + "+"
        else:
            books_url += "\"\""

        response = requests.get(url=books_url + "intitle")
        data = response.json()
        items = data.get('items', None)  # useful response result

        print("|---Count of Books from Google Books --> " + str(len(items)))

        return items
    else:
        return []


def create_new_book_from_data(input_data):
    info = input_data.get('volumeInfo', None)
    if info is not None:
        authors = info.get('authors', [])
        if authors:
            authors_text = ",".join([str(author) for author in authors])
        else:
            authors_text = "NIL"
        img = info.get('imageLinks', [])
        book = {
            'title': info.get('title', "NIL"),
            'authors': authors_text,
            'image': img.get('thumbnail', ""),
            'desc': info.get('description', "NIL"),
            'count': 0
        }
        print("Got value from Google Books API ")
        print(book)
        return book
    else:
        print("|---Cannot retrieve info,ignoring this book!!")
        return None

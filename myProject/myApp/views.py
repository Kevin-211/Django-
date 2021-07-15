from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myApp.models import Book
from django.urls import reverse


def detail(request):
    book_list = Book.objects.order_by('pub_date')[:5]
    context = {'book_list':book_list}
    return render(request, 'myApp/detail.html', context)

def addBook(requset):
    if requset.method == 'POST':
        temp_name = requset.POST['name']
        temp_author = requset.POST['author']
        temp_pub_house = requset.POST['pub_house']
    
    from django.utils import timezone
    temp_book = Book(name=temp_name,
    author=temp_author,
    pub_house=temp_pub_house,
    pub_date=timezone.now())
    temp_book.save()

    return HttpResponseRedirect(reverse('detail'))
# Create your views here.
def deleteBook(request, book_id):
    bookID = book_id

    Book.objects.filter(id=bookID).delete()
    return HttpResponseRedirect(reverse('detail'))
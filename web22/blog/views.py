from django.shortcuts import render
from blog.models import BookCategory, Book
from django.http import HttpResponse
import simplejson as json

def index(req):
    book_list = Book.objects.all()
    book_category_list = BookCategory.objects.all()
    first_book_category_list = [b for b in book_category_list if b.p_category is None]
    print first_book_category_list
    return render(req, 'index.html', {'book_list':book_list,'first_book_category_list':first_book_category_list})



def jsontest(req):
    if req.method == "POST":
        person = req.POST.get('person')
        person = json.loads(person)
        print req.POST, 'pst'
        print person, type(person), 'pp'
        person = json.dumps(person)
        print person, type(person),'ttttttttt'
        return HttpResponse(person)
    else :
        return render(req, "jsontest.html", {})

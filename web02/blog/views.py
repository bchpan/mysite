from django.shortcuts import render
from django.http import HttpResponse
import simplejson



def jsontest(req):
    if req.method == "POST":
        #assert False
        #users_session = req.session.get('users',[])
        user_session = []
        users = req.POST.get('users')
        users = simplejson.loads(users)
        #users_session.append(users)
        print users
        req.session['users'] = users
        return HttpResponse("ok")
    else:
        #assert False
        return render(req,"jsontest.html", {})


def jsontest1(req):
    jobs = req.session['jobs']
    print req.session['jobs']
    return render(req, "jsontest1.html", {'jobs':jobs})

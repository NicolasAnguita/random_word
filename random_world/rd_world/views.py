from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        rstring = get_random_string(length=14)

        if 'contador' in request.session:
            request.session['contador'] +=1
        else:
            request.session['contador'] = 1
        
        context = {
            "rdstring": rstring
        }
        return render(request, "index.html", context)
        
    if request.method == "POST":
        print("a POST request is being made to this route")
        del request.session['contador']
        return redirect("/random_world")
    
    

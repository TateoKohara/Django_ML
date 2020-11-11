from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    if request.method == "GET":
        return render(
            request,
            "ML_ai/home.html"
        )
    else:    
        title = request.POST["title"]
        return render(
            request,
            "ML_ai/home.html",
            {"title": title.split()}
        )
    

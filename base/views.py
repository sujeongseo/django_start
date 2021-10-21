from django.shortcuts import render

def base(request):
    context = {

    }

    return render(request, "base.html", context)

def inherit(request):
    context = {

    }
    return render(request, "base_ih.html",context)
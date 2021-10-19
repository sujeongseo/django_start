from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "shopping/index.html")

def admin(request):
    return render(request, "shopping/admin.html")

def item(request):
    return render(request, "shopping/item.html")
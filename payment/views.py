from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "payment/index.html")

def purchase(request):
    return render(request, "payment/purchase.html")

def complete(request):
    return render(request, "payment.complete.html")

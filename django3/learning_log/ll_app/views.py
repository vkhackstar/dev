from django.shortcuts import render

# Create your views here.

def index(request):
    """ home page for ll_app """
    return render(request, 'll_app/index.html')

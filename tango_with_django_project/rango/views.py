from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    context_dict = {
        'aboldmessage': 'crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, "rango/index.html", context=context_dict)


def about(request):
    context_dict = {
        'aboutmessage': 'happy, happy and happy!!'
    }
    return render(request, "rango/about.html", context=context_dict)




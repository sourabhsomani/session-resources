from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Hello</h1>")
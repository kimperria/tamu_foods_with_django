from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''
    Function view to display home page
    '''
    name = 'Tamu Eats'
    return render(request, 'tamueats/homepage.html', {"name": name})

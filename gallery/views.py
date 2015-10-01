from django.shortcuts import render
from django.shortcuts import render_to_response

def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html')

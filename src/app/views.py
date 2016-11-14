from django.shortcuts import render_to_response, render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})




from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def get_req(request):
    return HttpResponse(request.user)


def test(request):
    return render(request, 'test.html', {'variable': 'world'})


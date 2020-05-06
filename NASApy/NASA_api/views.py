from django.http import HttpResponse


def index(request):
    return HttpResponse("NASA, for the win!")

from django.shortcuts import render
from django.template import RequestContext
from main.models import Date


def index(request):
    if request.method == "POST":
        date_time = request.POST['date_time']
        new = Date(date_time=date_time)
        new.save()
    return render(request, 'main/index.html')

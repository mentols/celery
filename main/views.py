from datetime import datetime, timedelta
from django.shortcuts import render
from django.template import RequestContext
from main.models import Date
from main.tasks import *


def index(request):
    if request.method == "POST":
        date_time = request.POST['date_time']
        new = Date(date_time=date_time)
        new.save()
        eta = date_time[0:10] + ' ' + date_time[11:] + ':00'
        date_time_obj = datetime.strptime(eta, '%Y-%m-%d %H:%M:%S')
        date_time_obj -= timedelta(hours=3)
        adding_task.apply_async(args=(eta,), eta=date_time_obj)
    return render(request, 'main/index.html')

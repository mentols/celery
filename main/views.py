from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from django.template import RequestContext
from main.models import Date
from main.tasks import adding_task


def correct_timezone(local_time):
    utc_time = datetime.utcnow()
    correct = local_time - utc_time
    # print('Correct: ', round(correct.seconds/60/60))
    return round(correct.seconds/60/60)


def index(request):
    if request.method == "POST":
        date_time = request.POST['date_time'] + ':00'
        new = Date(date_time=date_time)
        new.save()
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S')
        date_time_obj -= timedelta(hours=correct_timezone(date_time_obj))
        adding_task.apply_async(args=(date_time,), eta=date_time_obj)
    return render(request, 'main/index.html')

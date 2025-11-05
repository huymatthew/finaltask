from django.shortcuts import render
import datetime

def games(request):
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    print(today.day, today.month, today.hour)
    context = {"show":True}
    if not (today.day == 9 and today.month == 11 and today.hour >= 14):
        context['show'] = False
    return render(request, 'games.html', context)
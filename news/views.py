from django.shortcuts import redirect, render
import datetime as dt
from django.http import Http404


# Create your views here.
def welcome(request):

    return render(request, 'welcome.html')

def news_of_day(request):

    date = dt.date.today()

    # day = convert_dates(date)

    context = {'date': date}

    return render(request, 'news_of_day.html', context)

# getting day of week

# def convert_dates(dates):
#     day_number = dt.date.weekday(dates)

#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friaday', 'Saturday', 'Sunday']

#     day = days[day_number]

#     return day

def past_days_news(request, past_date):

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == date.today():
        return redirect(news_of_day)

    context = {'date': date}

    return render(request, 'past_news.html', context)
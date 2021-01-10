from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photo_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})   

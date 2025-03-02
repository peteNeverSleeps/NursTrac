from django.shortcuts import render
from .models import HourLog, Activity
from .forms import HourLogForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Hours Index Page")

def log_hours(request):
    if request.method == 'POST':
        form = HourLogForm(request.POST)
        if form.is_valid():
            hourlog = form.save(commit=False)
            hourlog.user = request.user
            hourlog.save()
            return redirect('hours:timesheet')
    else:
        form = HourLogForm()
    return render(request, 'hours/log_hours.html', {'form': form})

def timesheet(request):
    logs = HourLog.objects.filter(user=request.user)
    return render(request, 'hours/timesheet.html', {'logs': logs})
# Create your views here.

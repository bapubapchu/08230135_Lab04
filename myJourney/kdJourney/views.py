from django.shortcuts import render
from .models import AboutMe, LearningJourney

def index(request):
    # Get all learning journey entries, ordered by date
    journeys = LearningJourney.objects.all().order_by('-date')
    return render(request, 'index.html', {'journeys': journeys})

def aboutMe(request):
    # Get all about me entries
    about_infos = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'about_infos': about_infos})
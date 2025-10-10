from django.shortcuts import render
from .models import LearningJourney

# Create your views here.
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})
def about_me(request):
    return render(request, 'aboutMe.html')

    

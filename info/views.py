from django.shortcuts import render
from .models import TeamMember, Affiliation, Publication

# Create your views here.

def index(request):
    context = {
        'members': TeamMember.objects.filter(user__is_active=True),
        'aff_logos': Affiliation.objects.all()
    }
    return render(request, 'info/index.html', context)

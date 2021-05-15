from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html', {})

def gig_detail(request, id):
    return render(request, 'gig_detail.html', {})
from django.shortcuts import render
from djangoModules.forms import Wanafunzi


def home(request):
    stu = Wanafunzi
    return render(request, 'index.html', {'form': stu})

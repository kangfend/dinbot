from django.shortcuts import render
from bot.models import History


def index(request):
    history = History.objects.filter(channel='#django-id')
    context = {
        'history': history,
    }
    return render(request, 'index.html', context)

from datetime import datetime

from models import Fanzine

def previous_fanzines(request):
    context = {}
    qs = Fanzine.objects.filter(date__lt=datetime.now())
    context['previous_fanzines'] = qs.all()
    return context

def next_fanzines(request):
    context = {}
    qs = Fanzine.objects.filter(date__gt=datetime.now())
    if request.user.is_staff and qs.count():
        context['next_fanzines'] = qs.all()
    return context

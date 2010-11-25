from datetime import datetime

from django import http
from django import shortcuts
from django import template

from models import *

def current_fanzine_details(request,
    template_name='fanzine/fanzine_details.html', extra_context=None):

    object = Fanzine.objects.filter(date__lte=datetime.now()).latest()

    context = {
        'object': object,
    }
    context.update(extra_context or {})

    return shortcuts.render_to_response(template_name, context,
        context_instance=template.RequestContext(request))

def fanzine_details(request,
    year, month, day, slug,
    template_name='fanzine/fanzine_details.html', extra_context=None):

    min_datetime = datetime(int(year), int(month), int(day), 0, 0, 0, 0)
    max_datetime = datetime(int(year), int(month), int(day), 23, 59, 59, 0)

    object = shortcuts.get_object_or_404(
        Fanzine, date__gte=min_datetime, date__lte=max_datetime, slug=slug)

    if not request.user.is_staff and object.date > date.today():
        return http.HttpResponseForbidden

    context = {
        'object': object,
    }
    context.update(extra_context or {})

    return shortcuts.render_to_response(template_name, context,
        context_instance=template.RequestContext(request))

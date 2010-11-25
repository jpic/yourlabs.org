from datetime import date

from django import shortcuts
from django import template

from models import *

def current_fanzine_details(request,
    template_name='fanzine/fanzine_details.html', extra_context=None):

    object = Fanzine.objects.filter(date__lte=date.today()).latest()

    context = {
        'object': object,
    }
    context.update(extra_context or {})

    return shortcuts.render_to_response(template_name, context,
        context_instance=template.RequestContext(request))

def fanzine_details(request,
   year, month, day, slug,
   template_name='fanzine/fanzine_details.html', extra_context=None):

   object = get_object_or_404(Fanzine, date=date(year, month, day), slug=slug)

   context = {
       'object': object,
   }
   context.update(extra_context or {})

   return shortcuts.render_to_response(template_name, context,
       context_instance=template.RequestContext(request))

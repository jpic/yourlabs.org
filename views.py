from django import shortcuts
from django import template
from django import http
from django.core import urlresolvers

def form(request, 
         form_class=None, 
         template_name='form.html', 
         success_url=None,
         success_url_name=None,
         success_message=None,
         extra_context=None):
    if not form_class:
        raise Exception("form_class is a mandatory argument")

    context = {}
    
    print request.session, request.META
    if 'previous_url' not in request.session.keys():
        request.session['previous_url'] = request.META['HTTP_REFERER']

    print request.session['previous_url']

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save(request)

            if request.user.is_authenticated() and success_message:
                request.user.message_set.create(message=success_message)

            if success_url_name:
                success_url = urlresolvers.reverse(success_url_name)
            if success_url:
                return http.HttpResponseRedirect(success_url)

            if request.session['previous_url']:
                previous_url = request.session.pop('previous_url')
                return http.HttpResponseRedirect(previous_url)
    else:
        form = form_class()

    context['form_class'] = form_class
    context['form'] = form
    context.update(extra_context or {})

    return shortcuts.render_to_response(
        template_name,
        context,
        context_instance=template.RequestContext(request)
    )

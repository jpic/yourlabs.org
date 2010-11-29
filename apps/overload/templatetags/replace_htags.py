import re

from django import template
register = template.Library()

def replace_htags(html):
    html = re.sub('<(/?)h1>', '<\\1h4>', html)
    html = re.sub('<(/?)h2>', '<\\1h4>', html)
    html = re.sub('<(/?)h3>', '<\\1h4>', html)
    return html
register.filter('replace_htags', replace_htags)

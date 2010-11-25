from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext as _

class Fanzine(models.Model):
    date = models.DateTimeField(verbose_name=_(u'publication date'))
    site = models.ForeignKey('sites.site', verbose_name=_(u'site'), default=1)
    title = models.CharField(max_length=100, verbose_name=_(u'title'))
    slug = models.CharField(max_length=100, verbose_name=_(u'slug'))
    editorial = models.TextField(verbose_name=_(u'editorial'), null=True, blank=True)
    editorial_author = models.ForeignKey('auth.user', verbose_name=_(u'author'), null=True, blank=True)
    template = models.CharField(max_length=30, verbose_name=_(u'template'), null=True, blank=True)

    class Meta:
        ordering = ('date',)
        get_latest_by = ('date',)
    
    def __unicode__(self):
        return self.title

class FanzinePost(models.Model):
    fanzine = models.ForeignKey(Fanzine, verbose_name=_(u'fanzine'))
    post = models.ForeignKey('planet.post', verbose_name=_(u'posts'))
    date_add = models.DateField(verbose_name=_(u'add date'), auto_now_add=True)
    date_edit = models.DateField(verbose_name=_(u'edit date'), auto_now=True)
    order = models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title

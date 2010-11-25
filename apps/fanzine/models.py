from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext as _

class Fanzine(models.Model):
    date = models.DateTimeField(verbose_name=_(u'publication date'))
    site = models.ForeignKey('sites.site', verbose_name=_(u'site'), default=1)
    slug = models.CharField(max_length=100, verbose_name=_(u'slug'))
    title = models.CharField(max_length=100, verbose_name=_(u'title'), null=True, blank=True)
    text = models.TextField(verbose_name=_(u'editorial'), null=True, blank=True)

    class Meta:
        ordering = ('date',)
        get_latest_by = ('date',)

    def __unicode__(self):
        return self.title

class FanzinePart(models.Model):
    tag = models.ForeignKey('tagging.tag', verbose_name=_(u'tag'))
    fanzine = models.ForeignKey(Fanzine, verbose_name=_(u'fanzine'), null=True, blank=True)
    text = models.TextField(verbose_name=_(u'editorial'), null=True, blank=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.text

class FanzinePartPost(models.Model):
    part = models.ForeignKey(FanzinePart, verbose_name=_(u'part'))
    post = models.ForeignKey('planet.post', verbose_name=_(u'posts'))
    order = models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.post.title

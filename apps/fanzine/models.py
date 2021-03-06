from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext as _
from django.core import urlresolvers

from tagging.models import Tag

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

    def get_absolute_url(self):
        return urlresolvers.reverse('fanzine_details', kwargs={
            'year': self.date.year,
            'month': self.date.month,
            'day': self.date.day,
            'slug': self.slug
        })

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

    def save(self, force_insert=False, force_update=False, using=None):
        Tag.objects.add_tag(self.post, self.part.tag)

        return super(FanzinePartPost, self).save(force_insert, force_update, using)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.post.title

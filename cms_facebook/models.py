from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FacebookPage(models.Model):
    name = models.CharField(max_length=255)
    pageid = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

class LikeBox(CMSPlugin):
    page = models.ForeignKey(FacebookPage, related_name='like_boxes', verbose_name=_("Facebook Page"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True, blank=True, help_text=_("Default: Auto Scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=587)
    connections = models.PositiveSmallIntegerField(_("Amount of Users"), default=10)
    stream = models.BooleanField(_("Show stream"), default=True)
    header = models.BooleanField(_("Show header"), default=True)
    
    def __unicode__(self):
        return "LikeBox (%s)" % (self.page.name)
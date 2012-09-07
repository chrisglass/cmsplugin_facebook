from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_facebook import models

class BasePlugin(CMSPluginBase):
    name = None

    def render(self, context, instance, placeholder):
        context.update({'instance': instance,
                        'name': self.name,
                        'url': instance.pageurl or \
                               context['request'].build_absolute_uri()})
        return context

class FacebookLikeBoxPlugin(BasePlugin):
    model = models.FacebookLikeBox
    name = 'Facebook Like Box'
    module = 'Facebook'
    render_template = 'cmsplugin_facebook/likebox.html'
    change_form_template = 'cmsplugin_facebook/likebox_change_form.html'

class FacebookLikeButtonPlugin(BasePlugin):
    model = models.FacebookLikeButton
    name = 'Facebook Like Button'
    module = 'Facebook'
    render_template = 'cmsplugin_facebook/likebutton.html'
    change_form_template = 'cmsplugin_facebook/likebutton_change_form.html'

plugin_pool.register_plugin(FacebookLikeBoxPlugin)
plugin_pool.register_plugin(FacebookLikeButtonPlugin)

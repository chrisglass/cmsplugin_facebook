from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_facebook import models

class BasePlugin(CMSPluginBase):
    name = None
    
    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

class FacebookLikeBoxPlugin(BasePlugin):
    model = models.FacebookLikeBox
    name = 'Facebook Like Box Plugin'
    render_template = 'cmsplugin_facebook/likebox.html'
        
class FacebookShareButtonPlugin(BasePlugin):
    model = models.FacebookShareButton
    name = 'Facebook "Share" button plugin'
    render_template = "cmsplugin_facebook/sharebutton.html"

class FacebookLikeButtonPlugin(BasePlugin):
    model = models.FacebookLikeButton
    name = 'Facebook Like Button Plugin'
    render_template = 'cmsplugin_facebook/likebutton.html'
    
plugin_pool.register_plugin(FacebookLikeBoxPlugin)
plugin_pool.register_plugin(FacebookLikeButtonPlugin)
plugin_pool.register_plugin(FacebookShareButtonPlugin)

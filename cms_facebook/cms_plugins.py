from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_facebook import models

class BasePlugin(CMSPluginBase):
    name = None
    render_template = 'cms_facebook/plugin.html'
    
    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

class LikeBoxPlugin(BasePlugin):
    model = models.LikeBox
    name = 'Facebook LikeBox Plugin'
    render_template = 'cms_facebook/likebox.html'
        
class ShareButtonPlugin(BasePlugin):
    model = models.ShareButton
    name = 'Facebook "Share" button plugin'
    render_template = "cms_facebook/sharebutton.html"

class LikeButtonPlugin(BasePlugin):
    model = models.LikeButton
    name = 'Facebook Like Button Plugin'
    render_template = 'cms_facebook/likebutton.html'
    
plugin_pool.register_plugin(LikeBoxPlugin)
plugin_pool.register_plugin(LikeButtonPlugin)
plugin_pool.register_plugin(ShareButtonPlugin)
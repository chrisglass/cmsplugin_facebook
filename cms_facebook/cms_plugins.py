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
    name = 'likebox'
    
    
class LikeButtonPlugin(BasePlugin):
    model = models.LikeButton
    name = 'like'
    
plugin_pool.register_plugin(LikeBoxPlugin)
plugin_pool.register_plugin(LikeButtonPlugin)
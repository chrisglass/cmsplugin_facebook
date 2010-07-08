from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_facebook import models

class BasePlugin(CMSPluginBase):
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

class LikeBoxPlugin(BasePlugin):
    model = models.LikeBox
    
plugin_pool.register_plugin(LikeBoxPlugin)
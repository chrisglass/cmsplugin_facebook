from django import template
from cms_facebook.utils import FacebookIFrameRenderer

register = template.Library()


class FacebookIFrameNode(template.Node):
    def __init__(self, instance, name):
        self.instance = instance
        self.name = name
        
    def render(self, context):
        request = context['request']
        instance = self.instance.resolve(context)
        name = self.name.resolve(context)
        renderer = FacebookIFrameRenderer(name)
        return renderer.render(request, context, instance) 


@register.tag
def render_facebook_iframe(parser, token):
    bits = token.split_contents()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("render_facebook_iframe takes exactly two arguments")
    return FacebookIFrameNode(*[parser.compile_filter(bit) for bit in bits[1:]])
import urllib
from django.conf import settings

class FacebookBaseRenderer(object):
    def __init__(self, name):
        self.name = name


class FBMLRenderer(FacebookBaseRenderer):
    """
    <fb:like-box
    profile_id="185550966885"
    width="567"
    connections="20"
    stream="false"
    header="false">
    </fb:like-box>
    """
    def __init__(self, name):
        super(FBMLRenderer, self).__init__(name)
        self.tagname = 'fb:%s' % self.name

class FacebookIFrameRenderer(FacebookBaseRenderer):
    scrolling = 'no'
    frameborder = '0'
    allowTransparency = 'true'
    default_styles = ['border:none;', 'overflow:hidden;']
    tagname = 'iframe'
    base_url = 'http://www.facebook.com/plugins/%s.php?%%s'
    
    def __init__(self, name):
        super(FacebookIFrameRenderer, self).__init__(name)
        self.src_template = self.base_url % self.name.replace('-','')

    def render(self, request, context, instance):
        attrs = [
            'src="%s"' % self.build_src(request, context, instance),
            'scrolling="%s"' % self.scrolling,
            'frameborder="%s"' % self.frameborder,
            'style="%s"' % self.build_style(request, context, instance),
            'allowTransparency="%s"' % self.allowTransparency,
        ]
        return '<%s %s></%s>' % (self.tagname, ' '.join(attrs), self.tagname)
        
    def build_src(self, request, context, instance):
        bits = self.build_src_bits(request, context, instance)
        return self.src_template % bits
        
    def build_src_bits(self, request, context, instance):
        bits = []
        for bit in instance.fb_bits:
            getter = instance.fb_aliases.get(bit, lambda r,c,i: getattr(i, bit))
            value = getter(request, context, instance)
            if isinstance(value, bool):
                value = 'true' if value else 'false'
            bits.append('%s=%s' % (bit, urllib.quote(str(value))))
        bits.append('height=%s' % instance.height)
        bits.append('width=%s' % self._get_width(request, context, instance))
        return '&'.join(bits)
    
    def build_style(self, request, context, instance):
        bits = []
        for default in self.default_styles:
            bits.append(default)
        bits.append('width:%spx;' % self._get_width(request, context, instance))
        bits.append('height:%spx;' % instance.height)
        return ''.join(bits)
        
    def _get_width(self, request, context, instance):
        width = getattr(instance, 'width', None)
        if not width:
            return context.get('width', instance.fb_default_width)
        return width
    
    
def get_renderer(name):
    return RENDERER_CLASS(name)
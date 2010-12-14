from django import template
from django.template.loader import render_to_string

register = template.Library()
import settings

@register.simple_tag
def cms_facebook_likebox(likebox_name):
    from cms_facebook.models import LikeBox
    try:
        likebox = settings.CMS_FACEBOOK_LIKEBOX[likebox_name]
    except LookupError:
        return "LikeBox Settings not found"
    instance = LikeBox(**likebox)
    return render_to_string("cms_facebook/likebox.html", {"instance" : instance})


@register.simple_tag
def cms_facebook_likebutton(likebutton_name):
    from cms_facebook.models import LikeButton
    try:
        likebutton = settings.CMS_FACEBOOK_LIKEBUTTON[likebutton_name]
    except LookupError:
        return "LikeButton Settings not found"
    instance = LikeButton(**likebutton)
    return render_to_string("cms_facebook/likebutton.html", {"instance" : instance})
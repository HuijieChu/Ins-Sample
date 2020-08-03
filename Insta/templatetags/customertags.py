from Insta.models import Like
from django import template

register = template.Library()
@register.simple_tag
def has_user_linked_post(post,user):
    try:
        like = Like.objects.get(user=user,post=post)
        return 'fa-heart'
    except:
        return 'fa-heart-o'
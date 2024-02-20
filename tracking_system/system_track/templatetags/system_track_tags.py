from django.template import Library

register = Library()


@register.inclusion_tag(name='header_tags', filename='header.html')
def header_tags(user, header):
    if not header:
        header='home'

    return {'header': header, 'user':user}

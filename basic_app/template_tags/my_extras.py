from django import template

register = template.Library()

@register.filter(name='cut') #oooh decorators
def cut(value, arg):
    """
    This cuts out all values of Arg from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)

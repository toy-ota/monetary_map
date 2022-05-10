from django import template
 
 
register = template.Library()
 
@register.filter(name="calculate_tax")
def calculate_tax(value, args):
    return value * (args+1)

@register.filter(name="add_super")
def add_super(args):
    return "superID_" + str(args)
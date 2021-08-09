from django import template
register = template.Library()

@register.filter
def get_response(responses, pk):
    return responses.get(answer__pk = pk).answer
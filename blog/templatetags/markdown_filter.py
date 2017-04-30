from django import template
import markdown
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text)
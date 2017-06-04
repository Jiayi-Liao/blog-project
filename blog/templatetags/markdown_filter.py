from django import template
import markdown
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    format_text = markdown.markdown(text, extensions=['markdown.extensions.codehilite', 'markdown.extensions.fenced_code'])
    return format_text
from django import template
import re
register = template.Library()

@register.filter
def format_telefone(value):
    digits = ''.join(filter(str.isdigit, str(value)))
    if len(digits) == 11:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    return value


@register.filter
def remove_chars(value):
    if not value:
        return ''
    return re.sub(r'\D', '', value)  # Remove tudo que não é número

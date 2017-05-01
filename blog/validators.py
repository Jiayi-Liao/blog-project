from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_min_length(value):
    if len(value) < 10:
        raise ValidationError(
            _('%(value)s length shorter than 10'),
            params={'value': value},
        )

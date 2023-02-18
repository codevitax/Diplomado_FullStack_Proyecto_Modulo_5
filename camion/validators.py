from django.core.exceptions import ValidationError


def validar_cuatro_cifras(value):
    if value < 1000 != 0:
        raise ValidationError(
            '%(value)s no hay placas menores a 1000',
            params={'value': value},
        )
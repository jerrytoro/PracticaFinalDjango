from django.core.exceptions import ValidationError

def validar_creditos(value):
    if value > 10:
        raise ValidationError(
            '%(value)s exede la cantidad de creditos',
            params={'value':value}
        )
    if value <=0:
        raise ValidationError(
            'los creditos tienen que ser mayor a 0',
            params={'value':value}
        )


def validar_ci(value):
    if len(value)<=4:
        raise ValidationError(
            'ingrese un carnet con mas de 3 digitos',
            params={'value':value}
        )


def validar_codigo(value):
    if len(value)<3:
        raise ValidationError(
            'ingrese un cogido numerico de 3 dijitos ',
            params={'value':value}
        )
    
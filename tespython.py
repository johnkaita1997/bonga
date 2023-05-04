def transform_phone_number(phone_number):
    if not phone_number:
        return phone_number
    if phone_number == "":
        return phone_number
    if phone_number.startswith('0'):
        return '254' + phone_number[1:]
    elif phone_number.startswith('+254'):
        return phone_number[1:]
    else:
        return phone_number



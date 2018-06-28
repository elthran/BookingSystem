import wtforms.validators


def check_currency_format(form, field):
    """Assert that a currency field only has 2 decimal places."""
    try:
        num_of_decimals = str(field.data).rsplit('.')[1]
    except IndexError:
        num_of_decimals = ''
    if len(num_of_decimals) > 2:
        raise wtforms.validators.ValidationError('Only 2 decimal places are allowed for currency fields.')

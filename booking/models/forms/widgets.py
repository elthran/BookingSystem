from wtforms import widgets

from booking.models.formats import format_as_currency


class CurrencyInput(widgets.TextInput):
    """Format any passed value as currency."""

    def __call__(self, field, **kwargs):
        if 'value' in kwargs:
            kwargs['value'] = format_as_currency(kwargs['value'])
        return super().__call__(field, **kwargs)

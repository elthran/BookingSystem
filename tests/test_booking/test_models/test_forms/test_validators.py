import pytest
import wtforms.validators

from booking.models.forms.validators import check_currency_format


class MockField:
    """Replicate enough of a field object for testing."""
    def __init__(self, data):
        self.data = data


class TestCheckCurrency:
    def test_3_decimal_places(self):
        with pytest.raises(wtforms.validators.ValidationError):
            check_currency_format(None, MockField("55.555"))

    def test_2_decimal_places(self):
        assert check_currency_format(None, MockField("55.55")) is None

    def test_no_decimal_places(self):
        assert check_currency_format(None, MockField("55")) is None
        assert check_currency_format(None, MockField("55.")) is None

import pytest
from apps.creditcard import is_valid_credit_card  # Replace 'your_module' with the actual module name

@pytest.mark.parametrize("card_number,expected", [
    ("4532015112830366", True),  # Valid Visa
    ("6011111111111117", True),  # Valid Discover
    ("371449635398431", True),   # Valid Amex
    ("5555555555554444", True),  # Valid MasterCard
    ("4111111111111111", True),  # Another valid Visa
    ("4532015112830367", False), # Invalid - Luhn fail
    ("6011000990139425", False), # Invalid - altered last digit
    ("1234567812345670", False), # Invalid random
    ("4111-1111-1111-1111", True),  # Valid Visa with dashes
    ("4111 1111 1111 1111", True),  # Valid Visa with spaces
    ("", False),  # Empty string
    ("abcd efgh ijkl mnop", False),  # Non-numeric input
])
def test_is_valid_credit_card(card_number, expected):
    assert is_valid_credit_card(card_number) == expected

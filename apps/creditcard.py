# Luhn Algorithm to validate credit card numbers
def is_valid_credit_card(card_number: str) -> bool:
    digits = [int(d) for d in card_number if d.isdigit()]
    if not digits
        return False
        
    checksum = 0
    reverse_digits = digits[::-1]

    for i, d in enumerate(reverse_digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d

    return checksum % 10 == 0
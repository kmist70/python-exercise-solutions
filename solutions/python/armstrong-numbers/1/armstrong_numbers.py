def is_armstrong_number(number):
    str_number = str(number)
    num_digits = len(str_number)
    sum = 0
    i = 0
    while i < num_digits:
        digit_as_int = int(str_number[i])
        sum += digit_as_int ** num_digits
        i += 1
    if number == sum:
        return True
    return False

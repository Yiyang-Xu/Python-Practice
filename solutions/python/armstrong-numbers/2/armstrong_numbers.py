def is_armstrong_number(number):
    strNumb = str(number)
    power = len(strNumb)
    total = 0
    for digit in strNumb:
        total += int(digit) ** power
    return total == number

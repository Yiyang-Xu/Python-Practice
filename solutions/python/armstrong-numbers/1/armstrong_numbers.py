def is_armstrong_number(number):
    strNumb = str(number)
    power = len(strNumb)
    sum = 0
    for digit in strNumb:
        sum += int(digit) ** power
    return sum == number

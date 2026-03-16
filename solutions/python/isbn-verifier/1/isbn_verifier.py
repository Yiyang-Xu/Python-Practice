def is_valid(isbn):
    cleaned = isbn.replace('-', '')
    # check if the length is 10
    if len(cleaned) != 10:
        return False

    # create a list to store all numbers
    list_isbn = [char for char in cleaned if char.isdigit()]
    if cleaned.endswith('X'):
        list_isbn.append(10)

    sum = 0
    for indx, digit in enumerate(list_isbn):
        sum += (10-indx) * int(digit)
    return (sum % 11 == 0) and len(list_isbn) == 10
        

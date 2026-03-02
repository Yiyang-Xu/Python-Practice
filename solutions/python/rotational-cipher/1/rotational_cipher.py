def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in text:
        if char.islower():
            old_indx = alphabet.index(char)
            new_indx = (old_indx + key) % 26
            result += alphabet[new_indx]
        elif char.isupper():
            old_indx = alphabet.index(char.lower())
            new_indx = (old_indx + key) % 26
            result += alphabet[new_indx].upper()
        else:
            result += char
    return result

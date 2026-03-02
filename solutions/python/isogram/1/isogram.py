def is_isogram(string):
    cleaned = [char.lower() for char in string if char.isalpha()]
    str_set = set(cleaned)
    return len(str_set) == len(cleaned)

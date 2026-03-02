def transform(legacy_data):
    new_dict = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            lower_letter = letter.lower()
            new_dict[lower_letter] = score
    return dict(sorted(new_dict.items()))
        

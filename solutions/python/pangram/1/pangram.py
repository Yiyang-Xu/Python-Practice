def is_pangram(sentence):
    count = set()
    for ch in sentence:
        if ch.isalpha():
            count.add(ch.lower())
    return len(count) == 26
        

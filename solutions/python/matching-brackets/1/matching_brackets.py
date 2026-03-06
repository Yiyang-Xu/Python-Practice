def is_paired(input_string):
    pairs = {']':'[', '}':'{', ')':'('}
    left = pairs.values()
    right = pairs.keys()
    
    stack = []
    for char in input_string:
        if char in left:
            stack.append(char)
        elif char in right:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

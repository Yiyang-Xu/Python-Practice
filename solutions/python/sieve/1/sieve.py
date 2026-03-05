def primes(limit):
    result = []
    marked = set()
    if limit < 2:
        return result
    all_num = [i for i in range(2, limit+1)]
    for num in all_num:
        multiple = 2
        while num * multiple <= limit:
            marked.add(num * multiple)
            multiple += 1
    for num in all_num:
        if num not in marked:
            result.append(num)
    return result

def sum_of_multiples(limit, multiples):
    total_set = set()
    for multiple in multiples:
        total_set = total_set.union(find_multiples(limit, multiple))
    return sum(total_set)
        


def find_multiples(limit, multiple):
    result = set()
    if multiple >= limit:
        return result
    for i in range(1, limit):
        if multiple * i < limit:
            result.add(multiple * i)
    return result
        
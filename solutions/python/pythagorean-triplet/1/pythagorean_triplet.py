def triplets_with_sum(number):
    triplets = []
    for a in range(1, number//3):
        numerator = 2*number*a - number**2
        denominator = 2*a - 2*number
        if numerator % denominator == 0:
            b = int(numerator / denominator)
            if b > a:
                triplets.append([a, b, number-a-b])
    return triplets
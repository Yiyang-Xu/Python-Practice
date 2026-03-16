def square_root(number):
    if number <= 0:
        return
    l = 0
    r = number + 1
    while l != r-1:
        mid = (l+r) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            l = mid
        else: r = mid
    return
            

def equilateral(sides):
    if isTriangle(sides):
        a,b,c = sides
        if a==b and b==c and a==c:
            return True
    return False


def isosceles(sides):
    if isTriangle(sides):
        a,b,c = sides
        if a==b or b==c or a==c:
            return True
    return False


def scalene(sides):
    if isTriangle(sides):
        a,b,c = sides
        if a!=b and b!=c and a!=c:
            return True
    return False

def isTriangle(sides):
    for side in sides:
        if side <= 0:
            return False
    if sum(sides) > 2 * max(sides):
        return True
    else: return False
    
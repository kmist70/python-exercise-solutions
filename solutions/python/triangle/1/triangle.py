def equilateral(sides):
    if valid_sides(sides):
        a, b, c = sides
        if a == b and b == c:
            return True
    return False

def isosceles(sides):
    if valid_sides(sides):
        if equilateral(sides):
            return True
        a, b, c = sides
        if a == b and a != c or a == c and a != b or b == c and b != a:
            return True
    return False

def scalene(sides):
    if valid_sides(sides):
        a, b, c = sides
        if a != b and b != c and a != c:
            return True
    return False

def valid_sides(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    return True
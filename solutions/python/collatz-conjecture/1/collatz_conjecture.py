def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    result = number
    while result != 1:
        if result % 2 == 0:
            result /= 2
        else:
            result = 3 * result + 1
        steps += 1
    
    return steps

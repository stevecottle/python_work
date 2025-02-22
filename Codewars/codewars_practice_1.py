

def past(h, m, s):
    s = s * 1000
    m = m * 60000
    h = h * 3600000
    return h + m + s

result = past(1, 1, 1)
print(result)





def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False

result = zero_fuel(50, 25, 2)
print(result)


# Challenge: Solve Sum of Two Lowest Positive Integers 

def function_name(numbers):
    numbers.sort()
    return numbers[0] + numbers [1]

result = function_name([19, 5, 42, 2, 77])
print(result)



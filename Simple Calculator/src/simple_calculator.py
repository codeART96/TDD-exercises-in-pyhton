# this function adds more than two numbers
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# this function multiplies more than two numbers
def multiply(*args):
    sum = 1
    for i in args:
        sum *= i
    return sum

print(multiply(10, 5))
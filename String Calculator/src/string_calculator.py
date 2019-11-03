import re

def add(*numbers_string):
    if len(numbers_string) == "":
        return 0
    
    elif len(numbers_string) == 1:
        return int(numbers_string)
    
    elif numbers_string[0] == "/":
        result = 0
        delim = ""
        lines = numbers_string.split("\n")
        for char in range(2, len(lines[0])):
            delim = delim + lines[0][char]
        numbers = lines[1].split(delim)
        return multiple_numbers(numbers)
    
    else:
        result = 0
        delim = ","
        if numbers_string[1] != ",":
            delim = "\n"
        numbers = numbers_string.split(delim)
        return multiple_numbers(numbers)

def multiple_numbers(*numbers):
    result = 0 
    for num in numbers:
        result += int(num)
    return result
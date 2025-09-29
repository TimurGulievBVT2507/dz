def max_of_two(number):
    frst = int(input('Enter the first number: '))
    scnd = int(input('Enter the second number: '))
    if frst > scnd:
        return frst
    elif scnd > frst:
        return scnd
    else:
        return "The numbers are equal"
print(max_of_two(1))
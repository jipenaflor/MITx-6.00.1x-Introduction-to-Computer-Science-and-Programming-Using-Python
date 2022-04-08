#Implement a function that meets the specifications below:

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    total = 0
    for dig in s:
        if dig.isdigit():
            total += int(dig)
        else:
            if not any(char.isdigit() for char in s):
                raise ValueError
    return total

print(sum_digits("a;jk"))

""" Write a recursive function called raise_power() that takes in
two integer parameters, the first parameter being the base number
 and the second parameter being the power you want to raise it to.
This function will return the number raised to the given power. For
 example, if you called raise_power(4, 2) you would get 16 returned
which is 4^2. Remember to think about what the base and recursive
 cases will be and start with an iterative approach if you don't
know where to begin."""

# best solution
def raise_power(base, power):
    return base ** power

# iterative
def raise_power_interative(base, power):
    i = 1
    if power != 0:
        while i < power:
            base *= base
            i += 1
    else:
        base = 1
    return base

# recursive
def raise_power_recursive(base, power, count=1):
    # anything to the power of zero equals one
    if power == 0:
        return 1
    elif count < power:
        return raise_power_recursive(base * base, power, count + 1)
    else:
        return base

print(raise_power(4, 2))
print(raise_power_interative(4, 2))
print(raise_power_recursive(4, 2))

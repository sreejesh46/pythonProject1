number = 12345
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print("The sum of the digits is:", sum)

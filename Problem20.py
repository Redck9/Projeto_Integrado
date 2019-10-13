""" 

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

# We will first define a factorial function.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

#Calc factorial of 100

number = fact(100)

#Convert that number to a string so we can iterate

numberConverted = str(number)

soma = 0

for x in numberConverted:
    soma = soma + int(x)
    
# Prints sum of those numbers

print(soma)



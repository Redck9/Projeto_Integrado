def is_prime(number):
    candidate_factor = 0
    amount_of_factors = 0
    while candidate_factor<number:
        #A += B is equivalent to A = A + B
        candidate_factor += 1
        #A little easier way of testing whether one number divides another evenly
        if number % candidate_factor == 0:
            amount_of_factors += 1
    if amount_of_factors == 2:
        return True
    else:
        return False

number=1
prime_total=0
#generates a list of numbers.
while number<100:
    number += 1
    if is_prime(number):
        prime_total += number
print prime_total

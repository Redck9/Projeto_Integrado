import math

def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError('Erro : base não válida')
    if digits == []:
        return digits
    num = 0
    digits.reverse()
    for n in range(len(digits)):
        if digits[n] >= input_base or digits[n] < 0:
            raise ValueError('Erro: base não válida')
        num += digits[n] * input_base**n

    m = 1

    while output_base**m < num:
        m += 1

    m -= 1

    newDigits = []

    n = m

    while n >= 0:
        newDigits.append(math.floor(num / output_base**n))
        num -= output_base**n * newDigits[-1]
        if num < 0:
            num = 0

        n -= 1

    if sum(newDigits) == 0:
        return []

        
    return newDigits

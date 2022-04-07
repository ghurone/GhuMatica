def simplify(n1:int, n2:int) -> tuple:
    a = n1
    b = n2
    r = 1

    while r != 0:
        r = a % b
        a, b = b, r

    return int(n1 / a), int(n2 / a)


def float_to_frac(num:float) -> tuple:
    num_str = str(num)

    if num_str.isnumeric():
        if '.' in num_str:
            num_split = num_str.split('.')
            
            if len(num_split) == 2:
                tam_dec = len(num_split[1])
                dec = int('1' + tam_dec * '0')
                numerador = int(str(num_split[0]) + str(num_split[1]))
                
                return numerador, dec
        else:
            return num, 1
    
    raise SyntaxError('Por favor, digite o número corretamente')


def prime_factors(n:int) -> list:
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

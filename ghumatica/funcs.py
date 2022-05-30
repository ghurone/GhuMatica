def simplify(n1:int, n2:int) -> tuple:
    """ Passados dois número inteiros, ele retorna a simplificação da divisão por um fator comum"""
    a = n1
    b = n2
    r = 1

    while r != 0:
        r = a % b
        a, b = b, r

    return int(n1 / a), int(n2 / a)


def float_to_rational(num:float) -> tuple:
    num_str = str(num)
    if is_number(num_str):
        if '.' in num_str:
            num_split = num_str.split('.')
            
            if len(num_split) == 2:
                tam_dec = len(num_split[1])
                dec = 10**tam_dec 
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

# FUNÇÕES PARA VERIFICAR O TIPO DO NÚMERO #

def is_number(num) -> bool:
    if not isinstance(num, (int, float)):
        if not isinstance(num, str):
            return False
        
        try:
            float(num)
            return True
        except:
            return False

    return True


def is_integer(num) -> bool:
    if is_number(num):
        if int(float(num)) == float(num):
            return True
    
    return False


def is_float(num) -> bool:
    if is_number(num):
        if not is_integer(num):
            return True
        
    return False
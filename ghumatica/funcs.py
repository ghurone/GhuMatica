def simplify(n1, n2):
    a = n1
    b = n2
    r = 1

    while r != 0:
        r = a % b
        a, b = b, r

    return int(n1 / a), int(n2 / a)

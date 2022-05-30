from ghumatica.funcs import simplify, float_to_rational, is_number


class Fraction:
    def __init__(self, num, den=1):
        if not (is_number(num) or is_number(den)):
            raise TypeError('Os parâmetros `num` e `den` precisam ser numéricos!')
        
        if den == 0:
            raise ZeroDivisionError('O denominador não pode ser zero!!')
        
        num = float_to_rational(num)
        den = float_to_rational(den)

        self._num = num[0] * den[1]
        self._den = den[0] * num[1]
        
        self._num, self._den = simplify(self._num, self._den)
    
    @property
    def numerador(self):
        return self._num
    
    @property
    def denominador(self):
        return self._den

    def __repr__(self):
        if self._num == 0:
            return '0'
        
        if self._den == 1:
            return f'{self._num}'
        
        return f'Fraction({self._num},{self._den})'

    def __str__(self):
        return f'{self._num}/{self._den}'

    def __int__(self):
        return int(self._num / self._den)

    def __float__(self):
        return self._num / self._den

    def __add__(self, other):
        if isinstance(other, Fraction):
            if other._den != self._den:
                den = self._den * other._den
                num = self._den * other._num + self._num * other._den

            else:
                den = self._den
                num = self._num + other._num

        elif isinstance(other, (int, float)):
            numerador, denominador = float_to_rational(other)

            if self._den != denominador:
                den = self._den * denominador
                num = self._den * numerador + self._num * denominador

            else:
                den = self._den
                num = self._num + numerador

        else:
            raise TypeError('A soma precisa ser numérica.')

        num, den = simplify(num, den)

        return Fraction(num, den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            den = self._den * other._den
            num = self._num * other._num

        elif isinstance(other, (int, float)):
            if other == 0:
                return 0

            den = self._den
            num = self._num * other

        else:
            raise TypeError('A multiplicação precisa ser numérica.')

        num, den = simplify(num, den)

        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            den = self._den * other._num
            num = self._num * other._den

        elif isinstance(other, (int, float)):
            den = self._den * other
            num = self._num

        else:
            raise TypeError('A divisão precisa ser numérica.')

        num, den = simplify(num, den)

        return Fraction(num, den)

    def __rtruediv__(self, other):
        return other * Fraction(self._den, self._num)

    def __floordiv__(self, other):
        if isinstance(other, Fraction):
            return (self._num * other._den) // (self._den * other._num)
        elif isinstance(other, (float, int)):
            return self._num // (self._den * other)

    def __rfloordiv__(self, other):
        return (other * self._den) // self._num

    def __pow__(self, outra):
        return self.__float__() ** outra.__float__()

    def __rpow__(self, outra):
        return outra.__float__() ** self.__float__()

    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self._num, self._den)

    def __abs__(self):
        return Fraction(abs(self._num), abs(self._den))

    def __trunc__(self):
        return abs(self._num) // self._den

    def __floor__(self):
        return self._num // self._den

    def __ceil__(self):
        return -(-self._num // self._den)

    def __round__(self, ndigits=None):
        if ndigits is None:
            floor, remainder = divmod(self._num, self._den)
            if remainder * 2 < self._den:
                return floor
            elif remainder * 2 > self._den:
                return floor + 1
            elif floor % 2 == 0:
                return floor
            else:
                return floor + 1

        shift = 10 ** abs(ndigits)
        if ndigits > 0:
            return Fraction(round(self * shift), shift)
        else:
            return Fraction(round(self / shift) * shift)

    def __eq__(self, outra):
        return self.__float__() == outra.__float__()

    def __ne__(self, other):
        return self.__float__() != other.__float__()

    def __lt__(self, outra):
        return self.__float__() < outra.__float__()

    def __gt__(self, outra):
        return self.__float__() > outra.__float__()

    def __le__(self, outra):
        return self.__float__() <= outra.__float__()

    def __ge__(self, outra):
        return self.__float__() >= outra.__float__()

    def __bool__(self, outra):
        return bool(self._num)

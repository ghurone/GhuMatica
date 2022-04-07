from funcs import simplify, float_to_frac

class Fraction:
    def __new__(cls, num, den=1):
        if isinstance(num, (float, int)) and isinstance(den, (float, int)) and den != 0:
            if abs(den) == 1 and isinstance(num, int):
                return num * den
        else:
            raise TypeError('Os parâmetros ´num´ e ´den´ precisam ser do tipo númerico.')

        return super(Fraction, cls).__new__(cls)

    def __init__(self, num, den=1):
        if isinstance(num, float) or isinstance(den, float):
            num = float_to_frac(num)
            den = float_to_frac(den)
    
            self.numerador = num[0] * den[1]
            self.denominador = den[0] * num[1]

        self.numerador, self.denominador = simplify(self.numerador, self.denominador)

    def __repr__(self):
        return f'Fraction({self.numerador},{self.denominador})'

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def __int__(self):
        return int(self.numerador / self.denominador)

    def __float__(self):
        return self.numerador / self.denominador

    def __add__(self, other):
        if isinstance(other, Fraction):
            if other.denominador != self.denominador:
                den = self.denominador * other.denominador
                num = self.denominador * other.numerador + self.numerador * other.denominador

            else:
                den = self.denominador
                num = self.numerador + other.numerador

        elif isinstance(other, (int, float)):
            numerador, denominador = self.float_to_frac(other)

            if self.denominador != denominador:
                den = self.denominador * denominador
                num = self.denominador * numerador + self.numerador * denominador

            else:
                den = self.denominador
                num = self.numerador + numerador

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
            den = self.denominador * other.denominador
            num = self.numerador * other.numerador

        elif isinstance(other, (int, float)):
            if other == 0:
                return 0

            den = self.denominador
            num = self.numerador * other

        else:
            raise TypeError('A multiplicação precisa ser numérica.')

        num, den = simplify(num, den)

        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            den = self.denominador * other.numerador
            num = self.numerador * other.denominador

        elif isinstance(other, float):
            den = self.denominador * other
            num = self.numerador

        else:
            raise TypeError('A divisão precisa ser numérica.')

        num, den = simplify(num, den)

        return Fraction(num, den)

    def __rtruediv__(self, other):
        return other * Fraction(self.denominador, self.numerador)

    def __floordiv__(self, other):
        if isinstance(other, Fraction):
            return (self.numerador * other.denominador) // (self.denominador * other.numerador)
        elif isinstance(other, (float, int)):
            return self.numerador // (self.denominador * other)

    def __rfloordiv__(self, other):
        return (other * self.denominador) // self.numerador

    def __pow__(self, outra):
        return self.__float__() ** outra.__float__()

    def __rpow__(self, outra):
        return outra.__float__() ** self.__float__()

    def __pos__(self):
        return Fraction(self.numerador, self.denominador)

    def __neg__(self):
        return Fraction(-self.numerador, self.denominador)

    def __abs__(self):
        return Fraction(abs(self.numerador), self.denominador)

    def __trunc__(self):
        if self.numerador < 0:
            return abs(self.numerador) // self.denominador
        else:
            return self.numerador // self.denominador

    def __floor__(self):
        return self.numerador // self.denominador

    def __ceil__(self):
        return -(-self.numerador // self.denominador)

    def __round__(self, ndigits=None):
        if ndigits is None:
            floor, remainder = divmod(self.numerador, self.denominador)
            if remainder * 2 < self.denominador:
                return floor
            elif remainder * 2 > self.denominador:
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
        return bool(self.numerador)

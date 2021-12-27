from math import sqrt, atan, sin, cos, e, log
from funcs import simplify


class Complex:
    def __new__(cls, re, im):
        if not(isinstance(re, (int, float, Fraction)) or isinstance(im, (int, float, Fraction))):
            raise TypeError('Os paramêtros precisam ser numéricos.')

        return super(Complex, cls).__new__(cls)

    def __init__(self, re, im):
        self._re = re
        self._im = im

    def __str__(self):
        if self._re == 0:
            s = f'{self._im}j'

        else:
            if self._im > 0:
                s = f'({self._re} + {self._im}j)'

            else:
                s = f'({self._re} - {abs(self._im)}j)'

        return s

    def __repr__(self):
        return str(self)

    def __int__(self):
        return Complex(int(self._re), int(self._im))

    def __float__(self):
        return Complex(float(self._re), float(self._im))

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self._im == 0 and self._re == self.__float__()

        elif isinstance(other, (complex, Complex)):
            return abs(self) == abs(other)

        raise TypeError("")

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self._im == 0 and self._re < other

        elif isinstance(other, (complex, Complex)):
            return abs(self) < abs(other)

        raise TypeError("")

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self._im == 0 and self._re > other

        elif isinstance(other, (complex, Complex)):
            return abs(self) > abs(other)

        raise TypeError("")

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self._im == 0 and self._re <= other

        elif isinstance(other, (complex, Complex)):
            return abs(self) <= abs(other)

        raise TypeError("")

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self._im == 0 and self._re >= other

        elif isinstance(other, (complex, Complex)):
            return abs(self) >= abs(other)

        raise TypeError("")

    def __pos__(self):
        return self

    def __neg__(self):
        return Complex(-self._re, -self._im)

    def __abs__(self):
        return self.modulo

    def __bool__(self):
        return self._re != 0 and self._im != 0

    def __add__(self, other):
        """Método para somar Complexos"""
        if isinstance(other, (int, float, Fraction)):
            re = self._re + other
            im = self._im

        elif isinstance(other, (complex, Complex)):
            re = self._re + other.real
            im = self._im + other.imag

        else:
            raise TypeError("")

        return Complex(re, im)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Método para subtrair Complexos"""
        return self + (-other)

    def __rsub__(self, other):
        return - self + other

    def __mul__(self, other):
        """Método para multiplicar Complexos"""
        if isinstance(other, (int, float, Fraction)):
            re = self._re * other
            im = self._im * other

        elif isinstance(other, (complex, Complex)):
            re = self._re * other.real - self._im * other.imag
            im = self._re * other.imag + self._im * other.real

        else:
            raise TypeError("")

        return Complex(re, im)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        """Método para dividir complexos"""
        if isinstance(other, (int, float, Fraction)):
            re = self._re / other
            im = self._im / other

        elif isinstance(other, (complex, Complex)):
            den = other.real ** 2 + other.imag ** 2
            re = (self._re * other.real + self._im * other.imag) / den
            im = (self._im * other.real - self._re * other.imag) / den

        else:
            raise TypeError('')

        return Complex(re, im)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float, Fraction)):
            den = self._re ** 2 + self._im ** 2
            re = (other * self._re) / den
            im = (-other * self._im) / den

        elif isinstance(other, complex):
            den = self._re ** 2 + self._im ** 2
            re = (other.real * self._re + other.imag * self._im) / den
            im = (other.imag * self._re - other.real * self._im) / den

        else:
            raise TypeError('')

        return Complex(re, im)

    def __pow__(self, other):
        """Método para exponenciação de complexos"""
        mod_z, theta = self.modulo, self.angulo

        if isinstance(other, (float, int, Fraction)):
            re = (mod_z ** other) * cos(other * theta)
            im = (mod_z ** other) * sin(other * theta)

        elif isinstance(other, (complex, Complex)):
            const = e ** (other.real * log(mod_z) - other.imag * theta)
            arg = other.real * theta + other.imag * log(mod_z)
            re = const * cos(arg)
            im = const * sin(arg)

        else:
            raise TypeError('')

        return Complex(re, im)

    def __rpow__(self, other):
        if isinstance(other, (int, float, Fraction)):
            const = other ** self._re
            re = const * cos(self._im * log(other))
            im = const * sin(self._im * log(other))

        elif isinstance(other, complex):
            mod_z = sqrt((other.real) ** 2 + (other.imag) ** 2)
            theta = atan(other.imag / other.real)

            const = e ** (self._re * log(mod_z) - self._im * theta)
            arg = self._re * theta + self._im * log(mod_z)
            re = const * cos(arg)
            im = const * sin(arg)

        else:
            raise TypeError('')

        return Complex(re, im)

    @property
    def conjugado(self):
        """Retorna o conjugado do número complexo"""
        return Complex(self._re, -self._im)

    @property
    def modulo(self):
        """Retorna o módulo do número complexo"""
        return sqrt(self * self.conjugado)

    @property
    def angulo(self):
        """Retorna o ângulo - em radianos - com a reta real."""
        return atan(self._im / self._re)

    @property
    def real(self):
        """Retorna a parte real do número complexo."""
        return self._re

    @property
    def imag(self):
        """Retorna a parte imaginária do número complexo."""
        return self._im


class Fraction:
    def __new__(cls, num, den=1):
        if isinstance(num, (float, int)) and isinstance(den, (float, int)) and den != 0:
            if abs(den) == 1 and isinstance(num, int):
                return num * den
        else:
            raise TypeError('Os parâmetros ´num´ e ´den´ precisam ser do tipo númerico.')

        return super(Fraction, cls).__new__(cls)

    def __init__(self, num, den=1):
        num = self.float_to_frac(num)
        den = self.float_to_frac(den)

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

    @staticmethod
    def float_to_frac(num):
        num_str = str(num)

        if '.' in num_str:
            num_split = num_str.split('.')
            if len(num_split) == 2:
                tam_dec = len(num_split[1])
                dec = int('1' + tam_dec * '0')
                numerador = int(str(num_split[0]) + str(num_split[1]))
                return numerador, dec
            else:
                raise SyntaxError('Por favor, digite o número corretamente')
        else:
            return num, 1


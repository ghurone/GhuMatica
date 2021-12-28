from numerical import *
from math import acos, degrees

NUM_TYPE = (float, int, Fraction, Complex, complex)


def valid_linha(lista):
    for elem in lista:
        if not isinstance(elem, NUM_TYPE):
            return False
    return True


def valid_matriz(lista):
    for lin in lista:
        if not valid_linha(lin):
            return False
    return True


class Vector:
    def __init__(self, vec=None, dim=None, valor=0):
        if isinstance(vec, list) and valid_linha(vec):
            self.vec = vec
            self.dim = len(vec)

        elif vec is None and isinstance(dim, int) and dim > 0 and isinstance(valor, NUM_TYPE):
            self.dim = dim
            self.vec = [valor for _ in range(dim)]

        else:
            raise TypeError('Ops, deu defeito kkk')

    def __str__(self):
        s = f'{self.__class__.__name__}('

        for i in range(self.dim):
            if i != self.dim - 1:
                s += str(self.vec[i]) + ', '
            else:
                s += str(self.vec[i]) + ')'

        return s

    def __repr__(self):
        return str(self)

    def __pos__(self):
        return self

    def __neg__(self):
        return Vector([-elem for elem in self.vec])

    def __getitem__(self, item):
        return self.vec[item]

    def __setitem__(self, item, value):
        self.vec[item] = value

    def __len__(self):
        return self.dim

    def __abs__(self):
        return sqrt(self.produto_escalar(self.conjugado()))

    def __eq__(self, other):
        if self.dim == other.dim:
            return abs(self) == abs(other)

    def __ne__(self, other):
        if self.dim == other.dim:
            return abs(self) != abs(other)

    def __lt__(self, other):
        if self.dim == other.dim:
            return abs(self) < abs(other)

    def __gt__(self, other):
        if self.dim == other.dim:
            return abs(self) > abs(other)

    def __le__(self, other):
        if self.dim == other.dim:
            return abs(self) <= abs(other)

    def __ge__(self, other):
        if self.dim == other.dim:
            return abs(self) >= abs(other)

    def __add__(self, other):
        if isinstance(other, Vector) and self.dim == other.dim:
            new = []
            for i in range(self.dim):
                new.append(self[i] + other[i])

            return Vector(new)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Vector) and self.dim == other.dim:
            return self.produto_escalar(other)

        elif isinstance(other, NUM_TYPE):
            new = [elem * other for elem in self.vec]

            return Vector(new)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, NUM_TYPE):
            new = [elem / other for elem in self.vec]

            return Vector(new)

    def produto_escalar(self, other):
        if isinstance(other, Vector) and self.dim == other.dim:
            soma = 0

            for i in range(self.dim):
                soma += self[i] * other[i]

            return soma

    def produto_vetorial(self, o):
        if isinstance(o, Vector) and self.dim == 3 and o.dim == 3:
            vec = [self[1] * o[2] - self[2] * o[1], self[2] * o[0] - self[0] * o[2], self[0] * o[1] - self[1] * o[0]]
            return Vector(vec)

    def conjugado(self):
        new = []
        for elem in self.vec:
            if isinstance(elem, (complex, Complex)):
                new.append(elem.conjugate())
            else:
                new.append(elem)

        return Vector(new)

    def angulo_entre(self, other, rad=True):
        if isinstance(other, Vector) and self.dim == other.dim:
            prod = self.produto_escalar(other)
            c = prod / (abs(self) * abs(other))

            return acos(c) if rad else degrees(acos(c))

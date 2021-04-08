import ghuerror

import math


class Vetor:

    def __init__(self, vetor: list = None, dim: int = None, value=None):
        if vetor and not dim and not value:
            self.dim = len(vetor)
            self.vetor = vetor
        elif dim and value and not vetor:
            self.dim = dim
            self.vetor = [value for _ in range(dim)]
        else:
            raise ghuerror.VetorError('Vetor inválido.')

    def __str__(self):
        s = 'Vetor('

        for i in range(self.dim):
            s += str(self.vetor[i]) + (', ' if i != self.dim - 1 else ')')

        return s

    def __repr__(self):
        return str(self)

    def __del__(self):
        del self

    def __getitem__(self, item):
        return self.vetor[item]

    def __setitem__(self, key, value):
        self.vetor[key] = value

    def __pos__(self):
        return self

    def __neg__(self):
        return Vetor([-e for e in self.vetor])

    def __abs__(self):
        return self.modulo()

    def __add__(self, other):
        if isinstance(other, Vetor):
            vetor = []
            for i in range(max(self.dim, other.dim)):
                comp = 0

                try:
                    comp += self.vetor[i]
                except IndexError:
                    comp += 0

                try:
                    comp += other.vetor[i]
                except IndexError:
                    comp += 0

                vetor.append(comp)

            return Vetor(vetor)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vetor):
            return self + (-other)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        if not isinstance(other, Vetor):
            vetor = [e * other for e in self.vetor]

            return Vetor(vetor)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Vetor):
            vetor = [e / other for e in self.vetor]

            return Vetor(vetor)

    def __itruediv__(self, other):
        return self / other

    def __floordiv__(self, other):
        if not isinstance(other, Vetor):
            vetor = [e // other for e in self.vetor]

            return Vetor(vetor)

    def __ifloordiv__(self, other):
        return self // other

    def __mod__(self, other):
        if not isinstance(other, Vetor):
            vetor = [e % other for e in self.vetor]

            return Vetor(vetor)

    def __imod__(self, other):
        return self % other

    def modulo(self):
        return math.sqrt(sum(math.pow(e, 2) for e in self.vetor))

    def versor(self):
        return self / self.modulo()

    def prod_escalar(self, other):
        if isinstance(other, Vetor):
            soma = 0

            for i in range(max(self.dim, other.dim)):
                try:
                    s = self.vetor[i]
                except IndexError:
                    s = 0

                try:
                    o = other.vetor[i]
                except IndexError:
                    o = 0

                soma += s * o

            return soma

    def prod_vetorial(self, other):
        if isinstance(other, Vetor) and self.dim == 3 and other.dim == 3:
            vetor = [self.vetor[1]*other.vetor[2] - self.vetor[2]*other.vetor[1],
                     self.vetor[2]*other.vetor[0] - self.vetor[0]*other.vetor[2],
                     self.vetor[0]*other.vetor[1] - self.vetor[1]*other.vetor[0]]

            return Vetor(vetor)

    def angulo_entre(self, other, grau=False):
        if isinstance(other, Vetor):
            prod = self.prod_escalar(other)
            pmod = self.modulo() * other.modulo()

            return math.degrees(math.acos(prod / pmod)) if grau else math.acos(prod / pmod)


if __name__ == '__main__':
    v = Vetor([1, 0, 0])
    u = Vetor([0, 0, 1])
    a = v.versor()

    print(v.prod_escalar(v))
    print(v.angulo_entre(u))
    print(v.angulo_entre(u, True))
    print(u.prod_vetorial(v))

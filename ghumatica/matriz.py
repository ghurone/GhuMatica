import ghuerror


class Matriz:

    def __init__(self, matriz: list = None, shape: tuple = None, value: (int, float, complex) = 0):
        if matriz and shape is None:
            self.__mat = matriz
            self.shape = (len(matriz), len(matriz[0]))

        elif shape and value and matriz is None:
            self.shape = shape
            self.__mat = [[value for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        else:
            raise ghuerror.MatrizError('Ops! Informações inválidas')

        self.nlin = self.shape[0]
        self.ncol = self.shape[1]

    def __getitem__(self, linha):
        return self.__mat[linha]

    def __del__(self):
        del self

    def __str__(self):
        s = '['
        for i in range(len(self.__mat)):
            if i == 0:
                s += str(self.__mat[i]) + ',\n'
            elif i == len(self.__mat) - 1:
                s += ' ' + str(self.__mat[i]) + ']'
            else:
                s += ' ' + str(self.__mat[i]) + ',\n'

        return s

    def __repr__(self):
        return str(self)

    def __pos__(self):
        return self

    def __neg__(self):
        matriz = [[-self.__mat[i][j] for j in range(self.ncol)] for i in range(self.nlin)]

        return Matriz(matriz)

    def __add__(self, other):
        if isinstance(other, Matriz):
            if other.shape == self.shape:
                matriz = []

                for i in range(self.nlin):
                    linha = []
                    for j in range(self.ncol):
                        linha.append(self.__mat[i][j] + other.__mat[i][j])

                    matriz.append(linha)

                return Matriz(matriz)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Matriz):
            if other.shape == self.shape:
                return self + (-other)

    def __isub__(self, other):
        return self - other

    def __matmul__(self, other):
        if isinstance(other, Matriz):
            if self.ncol == other.nlin:
                prod_matriz = []
                for i in range(self.nlin):
                    linha = []
                    for j in range(other.ncol):
                        soma = 0
                        for k in range(self.ncol):
                            soma += self.__mat[i][k] * other.__mat[k][j]
                        linha.append(soma)

                    prod_matriz.append(linha)

                return Matriz(prod_matriz)

    def __imatmul__(self, other):
        return self @ other

    def __mul__(self, other):
        if isinstance(other, Matriz):
            return self @ other

        else:
            new_matrix = []
            for i in range(self.nlin):
                linha = []
                for j in range(self.ncol):
                    linha.append(self.__mat[i][j] * other)

                new_matrix.append(linha)

            return Matriz(new_matrix)

    def __imul__(self, other):
        return self * other

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Matriz):
            new_matrix = []
            for i in range(self.nlin):
                linha = []
                for j in range(self.ncol):
                    linha.append(self.__mat[i][j] / other)

                new_matrix.append(linha)

            return Matriz(new_matrix)

    def __itruediv__(self, other):
        return self / other

    def __floordiv__(self, other):
        if not isinstance(other, Matriz):
            new_matrix = []
            for i in range(self.nlin):
                linha = []
                for j in range(self.ncol):
                    linha.append(self.__mat[i][j] // other)

                new_matrix.append(linha)

            return Matriz(new_matrix)

    def __ifloordiv__(self, other):
        return self // other

    def __mod__(self, other):
        if not isinstance(other, Matriz):
            new_matrix = []
            for i in range(self.nlin):
                linha = []
                for j in range(self.ncol):
                    linha.append(self.__mat[i][j] % other)

                new_matrix.append(linha)

            return Matriz(new_matrix)

    def __imod__(self, other):
        return self % other

    def determinante(self):
        if self.ncol == self.nlin:

            if self.nlin == 1:
                return self.__mat[0][0]

            else:
                det_total = 0

                for j in range(self.ncol):
                    sinal = 1 if j % 2 == 0 else -1
                    multi = sinal * self.__mat[0][j]

                    new_matriz = Matriz([self.__mat[i][:j] + self.__mat[i][j + 1:] for i in range(1, self.nlin)])
                    parcial_det = new_matriz.determinante()

                    det_total += multi * parcial_det

                return det_total

    def diag_principal(self):
        if self.nlin == self.ncol:
            soma = 0
            for i in range(self.nlin):
                soma += self.__mat[i][i]

            return soma

    def diag_secundaria(self):
        if self.nlin == self.ncol:
            soma = 0

            k = self.nlin - 1
            for i in range(self.nlin):
                soma += self.__mat[k][i]
                k -= 1

            return soma

    def transposta(self):
        result = [[self.__mat[j][i] for j in range(self.nlin)] for i in range(self.ncol)]

        return Matriz(result)

    def inversa(self):
        if self.nlin == self.ncol:
            det = self.determinante()
            matriz = []

            for i in range(self.nlin):
                linha = []
                for j in range(self.ncol):
                    const = (-1) ** (i+j+2)
                    new_mat = [[self.__mat[y][x] for y in range(self.ncol) if y != j] for x in range(self.nlin) if x != i]
                    det_parcial = Matriz(new_mat).determinante()

                    linha.append(const * det_parcial / det)

                matriz.append(linha)

            return Matriz(matriz)


if __name__ == '__main__':
    m1 = Matriz([[1, 3], [2, 0]])
    m2 = Matriz([[4, 1], [6, 2]])

    print(m1)
    print(m1.inversa())
    print(m1.inversa() * m1)

    print(m2)
    print(m2.inversa())
    print(m2.inversa() * m2)


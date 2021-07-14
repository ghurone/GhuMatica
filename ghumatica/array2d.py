import ghuerror


def verifica_matriz(matriz: list):
    if isinstance(matriz[0], list):
        m = len(matriz[0])
    else:
        return False

    for linha in matriz:
        if not isinstance(linha, list) or len(linha) != m:
            return False

    return True


class Array2D:
    def __init__(self, array: list = None, shape: tuple = None, valor: float = 0):
        if not array and isinstance(shape, (tuple, list)) and isinstance(valor, (int, float)):
            if len(shape) == 2:
                self.shape = shape
                self.array = [[valor] * self.shape[1] for _ in range(self.shape[0])]

        elif isinstance(array, list) and verifica_matriz(array):
            a_shape = (len(array), len(array[0]))
            self.shape = a_shape
            self.array = array

        else:
            raise ghuerror.ArrayError('Alguma coisa deu errado na hora de criar o seu array!')

    def __str__(self):
        s = 'Array2D(['
        ma = len(str(self.max()))
        mi = len(str(self.min()))

        m = ma if ma > mi else mi

        for i in range(len(self.array)):
            if i != 0:
                s += '         '

            for j in range(len(self.array[i])):
                s += f'{self.array[i][j]}'.center(2 + m)

            s += '\n' if i != len(self.array) - 1 else '])'

        return s

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.shape[0]

    def __getitem__(self, item):
        if isinstance(item, int):
            if self.shape[0] != 1:
                return Array2D([self.array[item]])
            else:
                return self.array[0][item]

        elif isinstance(item, tuple):
            if len(item) == 2:
                return self.array[item[0]][item[1]]

    def __neg__(self):
        m, n = self.shape
        new = [[- self.array[i][j] for j in range(n)] for i in range(m)]

        return Array2D(new)

    def __add__(self, other):
        if isinstance(other, Array2D):
            if self.shape == other.shape:
                m, n = self.shape
                matriz = [[self.array[i][j] + other.array[i][j] for j in range(n)] for i in range(m)]

                return Array2D(matriz)

        elif isinstance(other, (float, int)):
            m, n = self.shape
            matriz = [[self.array[i][j] + other for j in range(n)] for i in range(m)]

            return Array2D(matriz)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Array2D):
            if self.shape == other.shape:
                return self + (-other)

        elif isinstance(other, (float, int)):
            return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            new = [[elem * other for elem in linha] for linha in self.array]

            return Array2D(new)

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self * other

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            new = [[elem / other for elem in linha] for linha in self.array]

            return Array2D(new)

    def __floordiv__(self, other):
        if isinstance(other, (float, int)):
            new = [[elem // other for elem in linha] for linha in self.array]

            return Array2D(new)

    def __pow__(self, other):
        if isinstance(other, (float, int)):
            new = [[elem ** other for elem in linha] for linha in self.array]

            return Array2D(new)

    def __mod__(self, other):
        if isinstance(other, (float, int)):
            new = [[elem % other for elem in linha] for linha in self.array]

            return Array2D(new)

    def max(self):
        maxi = [max(linha) for linha in self.array]

        return max(maxi)

    def min(self):
        mini = [min(linha) for linha in self.array]

        return min(mini)


if __name__ == '__main__':
    teste = Array2D([[1, 0], [0, 1]])
    testudo = Array2D([[1, 24, 3], [4, 5, 67], [17, 8, 9]])
    testudo += testudo

    print(testudo)
    print(testudo[1])
    print(testudo[1][1])
    print(testudo[1, 1])

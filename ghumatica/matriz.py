from ghumatica.funcs import is_integer, is_number, is_float, is_integer


def valid_shape(shape) -> bool:
    if isinstance(shape, (tuple, list)) and len(shape) == 2:
        if is_integer(shape[0]) and is_integer(shape[1]):
            return True
        
    return False


def valid_matrix(matrix) -> bool:
    if isinstance(matrix, (list, tuple)) and len(matrix) > 0:
        if not isinstance(matrix[0], (list, tuple)):
            return False
        
        tam = len(matrix[0]) 
        
        for linha in matrix:
            if isinstance(linha, (list, tuple)):
                if tam != len(linha):
                    return False
                
                for elem in linha:
                    if not is_number(elem):
                        return False
            else:
                return False
        
        return True
    
    return False


class Linha:
    def __init__(self, linha) -> None:
        self.linha = linha

    def __add__(self, other):
        if isinstance(other, Linha) and len(other) == len(self):
            a = [other[i] + self[i] for i in range(len(self))]
            return Linha(a)

        raise ValueError('Algo de errado!')
        
    def __getitem__(self, i):
        return self.linha[i]
    
    def __len__(self):
        return len(self.linha)        
    

class Matriz:
    def __init__(self, matriz, shape=None, valor=None) -> None:
        if shape:
            if valid_shape(shape):
                self._shape == int(shape[0]), int(shape[1])  # Talvez um str pode ser passado
                self._nlin, self._ncol == self._shape
            else:
                raise ValueError('O parâmetro `shape` está errado')
            
            if is_number(valor):
                self._valor == float(valor) if is_float(valor) else int(float(valor))
            else:
                raise ValueError('O parâmetro `valor` precisa ser numérico.')
            
            self._matriz = [Linha([valor for _ in self._ncol]) for _ in self._nlin]
            
        elif matriz:
            if valid_matrix(matriz):
                self._shape = len(matriz), len(matriz[0])
                self._nlin, self._ncol = self._shape
                self._matriz = [Linha(matriz[i]) for i in self._nlin] 
            else:
                raise ValueError('O parâmetro `matriz` está errado')
                
        else:
            raise ValueError('Insira os parâmetros corretamente.')
        
    @property
    def shape(self):
        return self._shape
    
    def __str__(self) -> str:
        s = ''
        for linha in self._matriz:
            for elem in linha:
                s += f'{elem} '                
            s += '\n'
        
        return s
    
    def __repr__(self) -> str:
        return str(self)
    
    def __add__(self, other: object) -> object:
        if isinstance(other, Matriz):
            if self.shape == other.shape:
                mat = [ self._matriz[i] + other._matriz[i] for i in range(self._nlin) ]
                return Matriz(mat)
            
            raise ValueError('As matrizes tem formatos diferentes!')
        
        raise ValueError('Ops, só consigo somar Matrizes com Matrizes.')
    
    def __sub__(self, other: object) -> object:
        if isinstance(other, Matriz):
            if self.shape == other.shape:
                mat = [[self._matriz[i][j] - other._matriz[i][j] for j in range(self._ncol)] for i in range(self._nlin)]
                return Matriz(mat)
            
            raise ValueError('As matrizes tem formatos diferentes!')
        
        raise ValueError('Ops, só consigo subtrair Matrizes com Matrizes.')
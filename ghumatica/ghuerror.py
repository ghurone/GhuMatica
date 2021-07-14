class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class TipoInvalido(Error):
    def __init__(self, msg):
        super().__init__(msg)


class ArrayError(Error):
    def __init__(self, msg):
        super().__init__(msg)
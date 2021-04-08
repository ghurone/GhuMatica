class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class TipoInvalido(Error):
    def __init__(self, msg):
        super().__init__(msg)


class IntervaloInvalido(Error):
    def __init__(self, msg):
        super().__init__(msg)


class FechadoError(Error):
    def __init__(self, msg):
        super().__init__(msg)


class MatrizError(Error):
    def __init__(self, msg):
        super().__init__(msg)


class VetorError(Error):
    def __init__(self, msg):
        super().__init__(msg)

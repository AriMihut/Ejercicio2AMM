class Moneda:

    def cantidad_en_euros(self, cantidad):
        pass

class Dolar(Moneda):

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def cantidad_en_euros(self):
        return self.cantidad * 0.89

class Libra(Moneda):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def cantidad_en_euros(self):
        return self.cantidad * 1.20

class Yen(Moneda):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def cantidad_en_euros(self):
        return self.cantidad * 0.0078



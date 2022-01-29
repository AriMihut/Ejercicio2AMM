class Moneda:
    cantidad = None

    def cantidad_en_euros(cantidad):
        pass

class Dolar(Moneda):

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def cantidad_en_euros(cantidad):
        cantidad * 0,89

class Libra(Moneda):
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.cantidad_en_euros = cantidad_en_euros

class Yen(Moneda):
    def __init__(self, cantidad, cantidad_en_euros):
        self.cantidad = cantidad
        self.cantidad_en_euros = cantidad_en_euros



class Moneda:
    cantidad = None
    cantidad_en_euros = None

class Dolar(Moneda):

    def __init__(self, cantidad, cantidad_en_euros):
        self.cantidad = cantidad
        self.cantidad_en_euros = cantidad_en_euros



class Libra(Moneda):
    def __init__(self, cantidad, cantidad_en_euros):
        self.cantidad = cantidad
        self.cantidad_en_euros = cantidad_en_euros

class Yen(Moneda):
    def __init__(self, cantidad, cantidad_en_euros):
        self.cantidad = cantidad
        self.cantidad_en_euros = cantidad_en_euros



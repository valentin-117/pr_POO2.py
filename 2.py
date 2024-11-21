class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = float(cantidad)

    # Getters y setters
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        if nuevo_titular:
            self.__titular = nuevo_titular
        else:
            raise ValueError("El titular no puede estar vacío.")
    #metodos para analizar los datos
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return f"Titular: {self.__titular}, Cantidad: {self.__cantidad:.2f}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("No se puede ingresar una cantidad negativa.")

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


# Uso.
cuenta = Cuenta("Lopez obrador", 1000.50)
print(cuenta.mostrar())

cuenta.ingresar(500)
print(cuenta.mostrar())

cuenta.retirar(300)
print(cuenta.mostrar())

cuenta.ingresar(-200)  # Intenta ingresar numeros negativos
print(cuenta.mostrar())

cuenta.retirar(1500)  # Puede entrar en números rojos
print(cuenta.mostrar())

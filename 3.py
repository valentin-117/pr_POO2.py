#primer cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = float(cantidad)
    # getters Y setters
    def mostrar(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        #segunda cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = float(bonificacion)

    def esTitularValido(self, edad):
        return 18 <= edad < 25

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%"

    def retirar(self, cantidad, edad):
        if self.esTitularValido(edad):
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero: el titular no es válido.")

# Uso.
cuenta_joven = CuentaJoven("Alejandro Escobedo", 100000, 23)
print(cuenta_joven.mostrar())

cuenta_joven.ingresar(6544)
print(cuenta_joven.mostrar())

cuenta_joven.retirar(400, 12)  # Edad válida
print(cuenta_joven.mostrar())

cuenta_joven.retirar(200, 27)  # Edad no válida
print(cuenta_joven.mostrar())

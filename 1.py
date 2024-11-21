
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        if isinstance(nuevo_dni, str) and len(nuevo_dni) == 9:
            self.__dni = nuevo_dni
        else:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")

    # Métodos adicionales
    def mostrar(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}"

    def esMayorDeEdad(self):
        return self.__edad >= 18


# Ejemplo de uso
persona = Persona()
persona.nombre = "Frias Angel"
persona.edad = 25
persona.dni = "12345678A"

print(persona.mostrar())  # Muestra los datos de la persona
print("¿Es mayor de edad?", persona.esMayorDeEdad())  # Verifica si es mayor de edad

persona.edad = 17
print(persona.mostrar())
print("¿Es mayor de edad?", persona.esMayorDeEdad())

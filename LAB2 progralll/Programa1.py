

#1. Pedir al usuario que ingrese la información básica del perro, como nombre, raza, color, edad, etc.
#2. Determinar si el perro es grande o pequeño basado en su peso (menos de 10kg o más de 10kg).
#3. Mostrar en pantalla la información del perro, incluyendo si es un "Perro Grande" o "Perro Pequeño" y su estado de atención.


# Cuando se crea un abjeto de esta clase puede ingresar los datos el usuario
class Perro:
    def __init__(self, nombre, raza, color, edad, peso):  
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad
        self.peso = peso
        self.estado = "NO ATENDIDO"
        self.tamano = "Perro Grande" if peso > 10 else "Perro Pequeño" #Aqui si el mayor que 10 es perro grande

    def __str__(self):  # se convierte cadena debe ser __str__
        return (f"Nombre: {self.nombre}\nRaza: {self.raza}\nColor: {self.color}\n"
                f"Edad: {self.edad}\nPeso: {self.peso}kg\nEstado: {self.estado}\nTamaño: {self.tamano}")

#  Aqui Se le pide al usuario que ingrese la información del perro
nombre = input("Ingresa el nombre del perro: ")
raza = input("Ingresa la raza del perro: ")
color = input("Ingresa el color del perro: ")
edad = int(input("Ingresa la edad del perro: "))
peso = int(input("Ingresa el peso del perro en kg: "))

# Crear una instancia de la clase Perro con la información ingresada
perro = Perro(nombre, raza, color, edad, peso)

# Cambiar el estado del perro a "ATENDIDO"
perro.estado = "ATENDIDO"

# Mostrar la información del perro en pantalla
print("\nInformación del perro registrado:")
print(perro)

# 1. Definir la clase Vehiculo, que representa un auto vendido en el concesionario.
class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo, motor, color, combustible, transmision, precio_compra, origen):
        self.marca = marca  # Marca del vehículo
        self.modelo = modelo  # Modelo del vehículo
        self.anio = anio  # Año del vehículo
        self.tipo = tipo  # Tipo del vehículo (sedán, SUV, etc.)
        self.motor = motor  # Tipo de motor (eléctrico, gasolina, etc.)
        self.color = color  # Color del vehículo
        self.combustible = combustible  # Tipo de combustible (gasolina, diésel o tamnien eléctrico)
        self.transmision = transmision  # Tipo de transmisión (automática, manual)
        self.origen = origen  # Origen del vehículo (nacional o importado)
        self.precio_compra = precio_compra  # Precio de compra del vehículo
        self.precio_venta = round(precio_compra * 1.4, 2)  # Precio de venta con un margen de ganancia del 40%
        
        # Atributos fijos por ley
        self.ruedas = 4  # Todos los vehículos tienen 4 ruedas
        self.capacidad_pasajeros = 5  # Todos los vehículos tienen capacidad para 5 pasajeros

    def __str__(self):
        # Método para mostrar la información del vehículo de manera formateada
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\nTipo: {self.tipo}\n"
                f"Motor: {self.motor}\nColor: {self.color}\nCombustible: {self.combustible}\n"
                f"Transmisión: {self.transmision}\nOrigen: {self.origen}\n"
                f"Precio de Compra: ${self.precio_compra}\nPrecio de Venta: ${self.precio_venta}\n"
                f"Ruedas: {self.ruedas}\nCapacidad de Pasajeros: {self.capacidad_pasajeros} personas")

# 2. Solicitar al usuario la información del vehículo
print("Registro de Vehículo:")
marca = input("Ingrese la marca del vehículo: ")
modelo = input("Ingrese el modelo del vehículo: ")
anio = int(input("Ingrese el año del vehículo: "))
tipo = input("Ingrese el tipo de vehículo (sedán, SUV, etc.): ")
motor = input("Ingrese el tipo de motor (eléctrico, gasolina, etc.): ")
color = input("Ingrese el color del vehículo: ")
combustible = input("Ingrese el tipo de combustible (gasolina, diésel, eléctrico): ")
transmision = input("Ingrese el tipo de transmisión (automática, manual): ")
origen = input("Ingrese el origen del vehículo (nacional o importado): ")
precio_compra = float(input("Ingrese el precio de compra del vehículo: "))

# 3. Crear una instancia de la clase Vehiculo con la información ingresada
vehiculo = Vehiculo(marca, modelo, anio, tipo, motor, color, combustible, transmision, precio_compra, origen)

# 4. SE muestra la información del vehiculo registrado
print("\nInformación del vehículo registrado:")
print(vehiculo)

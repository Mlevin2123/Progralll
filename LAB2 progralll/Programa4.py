# 1.En esta clase se  Definila  clase Dispositivo
class Dispositivo:
    def __init__(self, tipo, modelo, memoria, procesador, pantalla, almacenamiento, precio_compra):
        self.tipo = tipo  # Tipo de dispositivo (celular, tablet,)
        self.modelo = modelo  # Modelo del dispositivo
        self.memoria = memoria  # Cantidad de memoria RAM
        self.procesador = procesador  # Tipo de procesador
        self.pantalla = pantalla  # Tamaño de la pantalla
        self.almacenamiento = almacenamiento  # Capacidad de almacenamiento
        self.precio_compra = precio_compra  # Precio de compra del dispositivo
        self.precio_venta = round(precio_compra * 1.7, 2)  # Precio de venta con un margen de ganancia del 70%
        
        # Atributos fijos
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR
        self.origen = "Importado"  # Todos los dispositivos son productos importados

    def __str__(self):
        # Método para mostrar la información del dispositivo de manera formateada
        return (f"Tipo: {self.tipo.capitalize()}\nModelo: {self.modelo}\nMemoria RAM: {self.memoria}\n"
                f"Procesador: {self.procesador}\nPantalla: {self.pantalla} pulgadas\n"
                f"Almacenamiento: {self.almacenamiento} GB\nPrecio de Compra: ${self.precio_compra}\n"
                f"Precio de Venta: ${self.precio_venta}\nMarca: {self.marca}\nOrigen: {self.origen}")

# 2. Se solicita aqui aal usuario la información del dispositivo
print("Registro de Dispositivo Electrónico:")
tipo = input("Ingrese el tipo de dispositivo (celular, tablet, portátil): ")
modelo = input("Ingrese el modelO del dispositivo: ")
memoria = input("Ingrese la cantidad de memoria RAM (en GB): ")
procesador = input("Ingrese el tipo de procesador: ")
pantalla = float(input("Ingrese el tamaño de la pantalla (en pulgadas): "))
almacenamiento = int(input("Ingrese la capacidad de almacenamiento (en Gb): "))
precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))

# 3. Esta es la instancia de la clase Dispositivo con la información ingresada
dispositivo = Dispositivo(tipo, modelo, memoria, procesador, pantalla, almacenamiento, precio_compra)

# 4. Mostrar la información del dispositivo registrado
print("\nInformación del dispositivo registrado:")
print(dispositivo)

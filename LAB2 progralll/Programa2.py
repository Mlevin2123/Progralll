


# 1. Definir la clase Articulo, que representa un cuaderno o un lápiz.
class Articulo:
    def __init__(self, tipo, especificacion, precio_compra):
        self.tipo = tipo  # El tipo de artículo (cuaderno o lápiz)
        self.especificacion = especificacion  # Detalles específicos, como el número de hojas o el tipo de lápiz
        self.precio_compra = precio_compra  # Precio de compra del artículo
        self.precio_venta = round(precio_compra * 1.30, 2)  # Precio de venta con un margen de ganancia del 30%
        
        # Marcas predeterminadas según el tipo de artículo
        if tipo == "cuaderno":
            self.marca = "HOJITAS"
        elif tipo == "lapiz":
            self.marca = "RAYAS"

    def __str__(self):
        # Método para mostrar la información del artículo de manera formateada
        return (f"Tipo: {self.tipo.capitalize()}\nEspecificación: {self.especificacion}\nMarca: {self.marca}\n"
                f"Precio de Compra: ${self.precio_compra}\nPrecio de Venta: ${self.precio_venta}")

# 2. Solicitar al usuario la información del primer artículo (cuaderno)
print("Registro de Cuadernos:")
tipo = "cuaderno"
especificacion = input("Ingrese la especificación del cuaderno (50 hojas o 100 hojas): ")
precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))

# Crear una instancia de la clase Articulo para el cuaderno
cuaderno = Articulo(tipo, especificacion, precio_compra)

# 3. Solicitar al usuario la información del segundo artículo (lápiz)
print("\nRegistro de Lápices:")
tipo = "lapiz"
especificacion = input("Ingrese la especificación del lápiz (grafito o colores): ")
precio_compra = float(input("Ingrese el precio de compra del lápiz: "))

#  SE HACE  UNA instancia de la clase Articulo para el lápiz
lapiz = Articulo(tipo, especificacion, precio_compra)

# 4. Bien en el print final se muestra la información de ambos artículos que han registrado
print("\nInformación del cuaderno registrado:")
print(cuaderno)

print("\nInformación del lápiz registrado:")
print(lapiz)

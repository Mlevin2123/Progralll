# 1. Definir la clase Jugador, que representa a un jugador de fútbol en el equipo.
class Jugador:
    def __init__(self, nombre, posicion, dorsal, edad, altura, peso, nacionalidad, pie_dominante, valor_mercado, goles):
        self.nombre = nombre  # Nombre del jugador
        self.posicion = posicion  # Posición en la que juega (puede ser defensa, pivote, delantero)
        self.dorsal = dorsal  # Número del jugador
        self.edad = edad  # Edad del jugador
        self.altura = altura  # Altura del jugador (en cm)
        self.peso = peso  # Peso del jugador en kg
        self.nacionalidad = nacionalidad  # Nacionalidad del jugador
        self.pie_dominante = pie_dominante  # Pie dominante del jugador 
        self.valor_mercado = valor_mercado  # Valor de mercado en millones de euros
        self.goles = goles  # Goles anotados por el jugador
    
    def __str__(self):
        # Este método es para mostrar la información del jugador de manera formateada
        return (f"Nombre: {self.nombre}\nPosición: {self.posicion}\nDorsal: {self.dorsal}\n"
                f"Edad: {self.edad} años\nAltura: {self.altura} cm\nPeso: {self.peso} kg\n"
                f"Nacionalidad: {self.nacionalidad}\nPie Dominante: {self.pie_dominante}\n"
                f"Valor de Mercado: €{self.valor_mercado}M\nGoles: {self.goles}")

# 2. Solicitar al usuario la información del jugador
print("Registro de Jugador de Fútbol!!!")
print("los datos que pide en numeros luego se le agregara las recpectivas medidas o longitudes (etc)")
nombre = input("Ingrese el nombre del jugador: ")
posicion = input("Ingrese la posición del jugador (puede ser defensa, pivote, delantero): ")
dorsal = int(input("Ingrese el número del dorsal (en números): "))
edad = int(input("Ingrese la edad del jugador (en números): "))
altura = float(input("Ingrese la altura del jugador (en numero): "))
peso = float(input("Ingrese el peso del jugador (en numero): "))
nacionalidad = input("Ingrese la nacionalidad del jugador: ")
pie_dominante = input("Ingrese el pie dominante (derecho/izquierdo): ")
valor_mercado = float(input("Ingrese el valor de mercado del jugador (en millones de euros): "))
goles = int(input("Ingrese la cantidad de goles anotados por el jugador (en números): "))

# 3. Crear una instancia de la clase Jugador con la información ingresada
jugador = Jugador(nombre, posicion, dorsal, edad, altura, peso, nacionalidad, pie_dominante, valor_mercado, goles)

# 4. Mostrar la información del jugador registrado
print("\nInformación del jugador registrado:")
print(jugador)

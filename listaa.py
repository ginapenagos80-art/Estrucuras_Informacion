class animales:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.anterior = None
        self.siguiente = None

class lista_animales:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nombre, especie, edad):
        nuevo = animales(nombre, especie, edad)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def mostrar(self):
        actual = self.primero
        while actual:
            print(f"{actual.nombre}\n{actual.especie}\n{actual.edad} años")
            actual = actual.siguiente

sistema = lista_animales()

while True:
    print("\nSistema de adopcion de animales")
    print("1. Registrar animal")
    print("2. Mostrar animales")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        edad = int(input("Edad: "))
        sistema.insertar(nombre, especie, edad)

    elif opcion == "2":
        sistema.mostrar()

    elif opcion == "3":
        break
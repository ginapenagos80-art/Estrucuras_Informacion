class Animal:
    def __init__(self, codigo, nombre, raza, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Raza: {self.raza}, Edad: {self.edad} años"

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class listaCircular:

    def __init__(self):
        self.primero = None

    def append(self, dato):
        nuevo = nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            nuevo.siguiente = self.primero  # se apunta a sí mismo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.primero  # el nuevo último apunta al primero
        print(f"Se ha agregado el animal: {dato.nombre} con código {dato.codigo}")

    def mostrar(self):
        if self.primero is None:
            print("La lista está vacía")
            return
        actual = self.primero
        while True:
            print(actual.dato)
            actual = actual.siguiente
            if actual == self.primero:
                break

milista = listaCircular()
milista.append(Animal("A001", "Firulais", "Labrador", 3))
milista.append(Animal("A002", "Michi", "Criollo", 1))
milista.append(Animal("A003", "Rocky", "Pastor Alemán", 5))
milista.append(Animal("A004", "Luna", "Siames", 2))
milista.mostrar()
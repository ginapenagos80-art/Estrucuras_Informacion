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

class lista:

    def __init__(self):
        self.primero = None

    def append(self, dato):

        nuevo = nodo(dato)
        if self.primero == None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            print(f"Se ha agregado el animal: {dato.nombre} con código {dato.codigo}")

    def mostrar(self):
        actual = self.primero
        while actual:
            print(actual.dato) 
            actual = actual.siguiente
            
milista = lista()
milista.append(Animal("A001", "Firulais", "Labrador", 3))
milista.append(Animal("A002", "Michi", "Criollo", 1))
milista.append(Animal("A003", "Rocky", "Pastor Alemán", 5))
milista.append(Animal("A004", "Luna", "Siames", 2))
milista.mostrar()
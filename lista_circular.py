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

    def eliminar(self, codigo):
            if self.primero is None:
                print("La lista está vacía")
                return
            actual = self.primero
            anterior = None
            while True:
                if actual.dato.codigo == codigo:
                    if anterior is None:  # Se elimina el primer nodo
                        if actual.siguiente == self.primero:  # Solo hay un nodo
                            self.primero = None
                        else:
                            # Encontrar el último nodo para actualizar su siguiente
                            ultimo = self.primero
                            while ultimo.siguiente != self.primero:
                                ultimo = ultimo.siguiente
                            self.primero = actual.siguiente
                            ultimo.siguiente = self.primero
                    else:
                        anterior.siguiente = actual.siguiente
                    print(f"Se ha eliminado el animal con código {codigo}")
                    return
                anterior = actual
                actual = actual.siguiente
                if actual == self.primero:
                    break
            print(f"No se encontró un animal con código {codigo}")
    

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

    def alimentar_todos(self):
        if self.primero is None:
            print("La lista está vacía")
            return
        actual = self.primero
        while True:
            print(f"Alimentando a {actual.dato.nombre}")
            actual = actual.siguiente
            if actual == self.primero:
                break

    def cuidar(self):
        if self.primero is None:
            print("La lista está vacía")
            return
        actual = self.primero
        while True:
            print(f"revisando a {actual.dato.nombre}")
            actual = actual.siguiente
            if actual == self.primero:
                break    

milista = listaCircular()
milista.append(Animal("A001", "Firulais", "Labrador", 3))
milista.append(Animal("A002", "Michi", "Criollo", 1))
milista.append(Animal("A003", "Rocky", "Pastor Alemán", 5))
milista.append(Animal("A004", "Luna", "Siames", 2))
milista.append(Animal("A005", "mougli", "serpiente", 1))
milista.mostrar()
milista.alimentar_todos()
milista.cuidar()
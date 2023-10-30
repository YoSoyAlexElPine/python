class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    # Getter para el nombre
    def get_nombre(self):
        return self.nombre

    # Setter para el nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    # Getter para los apellidos
    def get_apellidos(self):
        return self.apellidos

    # Setter para los apellidos
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

class Cliente(Persona):
    def __init__(self, nombre, apellidos, numCuenta, balance):
        super().__init__(nombre, apellidos)
        self.numCuenta = numCuenta
        self.balance = balance

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad)  # Convertir la entrada en un número flotante
            if(cantidad>0):
                self.balance += cantidad
            else:
                print("Introduce una cantidad mayor que cero")
        except ValueError:
            print("Error: Introduce un numero")
        except Exception:
            print("Error")

    def retirar(self, cantidad):
        cantidad = float(cantidad)  # Convertir la entrada en un número flotante
        self.balance -= cantidad

    def __str__(self):
        # Devuelve una cadena que representa el objeto Cliente
        return f"Nombre: {self.nombre} {self.apellidos}, Número de Cuenta: {self.numCuenta}, Balance: {self.balance}"

def menu():
    print("=================================")
    print("= 0. Informacion                =")
    print("= 1. Ingresar dinero            =")
    print("= 2. Retirar dinero             =")
    print("= 3. Salir                      =")
    print("=================================")

def comienzo():
    print("=== Creación de Cliente ===")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    numCuenta = input("Número de cuenta: ")
    balance = input("Balance: ")
    print()

    cliente = Cliente(nombre, apellidos, numCuenta, float(balance))  # Convertir balance a un número flotante

    print("Cliente creado :)")
    print()
    return cliente

if __name__ == '__main__':
    try:

        #cliente = comienzo()

        cliente= Cliente("manolo","Sanchez",123454321,3)


        eleccion = 0
        while eleccion != 3 or eleccion>2 or eleccion<0:

            if (eleccion>3 or eleccion<0):
                print(eleccion,"no es una opcion valida")

            menu()
            eleccion = int(input("Opción: "))  # Convertir la entrada en un número entero
            if eleccion == 1:
                cliente.depositar(input("Cantidad a depositar: "))
            elif eleccion == 2:
                cliente.retirar(input("Cantidad a Retirar: "))
            elif eleccion == 0:
                print(cliente)

        print("Chao")
    except Exception:
        print("Error")



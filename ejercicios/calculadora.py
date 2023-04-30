class Coche:
    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
    
    def acelerar(self, velocidad):
        if self.velocidad_actual + velocidad <= self.velocidad_maxima:
            self.velocidad_actual += velocidad
            print("Acelerando. Velocidad actual:", self.velocidad_actual)
        else:
            print("No se puede acelerar más. Velocidad máxima alcanzada.")
    
    def frenar(self, velocidad):
        if self.velocidad_actual - velocidad >= 0:
            self.velocidad_actual -= velocidad
            print("Frenando. Velocidad actual:", self.velocidad_actual)
        else:
            print("No se puede frenar más. Coche detenido.")
    
    def info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad máxima:", self.velocidad_maxima)
        print("Velocidad actual:", self.velocidad_actual)

class funciones():
    def menu():
        print("0. salir")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multoplicar")
        print("4. Dividir")
    def suma(a, b):
        return a+b

    def resta(a, b):
        return a-b

    def mult(a, b):
        return a*b

    def div(a, b):
        if b == 0:
            return "Infinito"
        if a == 0 and b == 0:
            return "Incierto"
        else: 
            return a/b
    
eleccion=999
while eleccion!=0:
    funciones.menu()
    eleccion=int(input("Numero -> "))
    if eleccion!=0:
        a=int(input("numero a = "))
        b=int(input("numero b = "))
        if eleccion==1:
            print("Resultado = ",funciones.suma(a,b))
        if eleccion==2:
            print("Resultado = ",funciones.resta(a,b))
        if eleccion==3:
            print("Resultado = ",funciones.mult(a,b))
        if eleccion==4:
            print("Resultado = ",funciones.div(a,b))
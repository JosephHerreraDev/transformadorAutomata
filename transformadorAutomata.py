lenguaje = input("Lenguaje del AFN: ")

estados = input("Estados del AFN: ")

estadoInicial = estados[0]

estadosFinal = estados[-1]

class Estado:
    def __init__(self, lenguaje, estados):
        self.transiciones = {}
        transicion = []
        for estado in estados:
            for simbolo in lenguaje:
                transicion = input("Transiciones del estado " + estado + " si entra " + simbolo + ": ")
                self.transiciones[estado, simbolo] = transicion
        print(self.transiciones)
    def regresarTransiciones(self):
        return self.transiciones

estado = Estado(lenguaje, estados)
tablaTransiciones = []
for estadoLocal in estados:
    for simbolo in lenguaje:
        tablaTransiciones.append(estado.regresarTransiciones()[estadoLocal, simbolo])

print("Estado\t", end="")
for simbolo in lenguaje:
    print(simbolo + "\t", end="")
print()
for estado in estados:
    print(estado + "\t", end="")
    for simbolo in lenguaje:
        print(tablaTransiciones.pop(0) + "\t", end="")
    print()
   
input("Presione enter para continuar...")
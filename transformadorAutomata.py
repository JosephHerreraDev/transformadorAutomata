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

    def regresarTransiciones(self):
        return self.transiciones

estado = Estado(lenguaje, estados)
tablaTransicionesResumida = []
tablaTransiciones = []
for estadoLocal in estados:
    for simbolo in lenguaje:
        tablaTransiciones.append(estado.regresarTransiciones())
        tablaTransicionesResumida.append(estado.regresarTransiciones()[estadoLocal, simbolo])

print("Estado\t", end="|")
for simbolo in lenguaje:
    print(simbolo + "\t", end="|")
print()
x = 0
for estado in estados:
    print(estado + "\t", end="|")
    for simbolo in lenguaje:
        print(tablaTransicionesResumida[x] + "\t", end="|")
        x = x + 1
    print()

diccionario_destino = {}

tablaTransicionesAFD = []
tablaEstadosAFD = []

for elemento in tablaTransiciones:
    diccionario_destino = elemento
for simbolo in lenguaje:
    tablaTransicionesAFD.append(diccionario_destino[estadoInicial, simbolo])

tablaEstadosAFD.append(estadoInicial)
tablaCombinada = []
for simbolo in lenguaje:
    for elemento in tablaTransicionesAFD:
        if elemento not in tablaEstadosAFD:
            tablaEstadosAFD.append(elemento)
            for estado in elemento:
                print(estado + " : " + diccionario_destino[estado, simbolo])
                tablaCombinada.append(diccionario_destino[estado, simbolo])
                print(tablaCombinada)
print(tablaEstadosAFD)
print(tablaTransicionesAFD)

# * 1. Carga el estado inicial
# * 2. Leer las transiciones que resultan
# * 3. Mientras uno de los estados no este en la lista de estados principales, agregarlo
# 4. Genera las transiciones conbinando las que ya tiene
# 5. Poner transiciones que ya tiene
# 6. Regresar al paso 2


input("Presione enter para continuar...")
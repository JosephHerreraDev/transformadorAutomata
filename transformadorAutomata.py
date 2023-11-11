lenguaje = input("Lenguaje del AFN: ")
estados = input("Estados del AFN: ")
estadoInicial = estados[0]
estadosFinal = estados[-1]

class Estado:
    def __init__(self, lenguaje, estados):
        self.transiciones = {}
        for estado in estados:
            transicion = input("Transiciones del estado " + estado + " separadas por coma: ")
            transiciones = transicion.split(',')
            for i, simbolo in enumerate(lenguaje):
                self.transiciones[estado, simbolo] = transiciones[i] if i < len(transiciones) else ''

    def regresarTransiciones(self):
        return self.transiciones

estado = Estado(lenguaje, estados)
tablaTransicionesResumida = []
tablaTransiciones = []
for estadoLocal in estados:
    for simbolo in lenguaje:
        tablaTransiciones.append(estado.regresarTransiciones())
        tablaTransicionesResumida.append(estado.regresarTransiciones()[estadoLocal, simbolo])

print("Automata Finito No Determinista")
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

def llamarLlenarEstadosAFD():
    for elemento in tablaTransicionesAFD:
        if elemento not in tablaEstadosAFD:
            llenarEstadosAFD(elemento)
            tablaEstadosAFD.append(elemento)
            llamarLlenarEstadosAFD()

def llenarEstadosAFD(elemento):
    retorno = ''
    for simbolo in lenguaje:
        for estado in elemento:
            for letra in diccionario_destino[estado, simbolo]:
                if letra not in retorno:
                    retorno += letra
        if retorno is not '':
            diccionario_destino[elemento, simbolo] = retorno
            tablaTransicionesAFD.append(diccionario_destino[elemento, simbolo])
            retorno = ''

llamarLlenarEstadosAFD()

print()
print("Automata Finito Determinista")
print("Estado\t", end="|")
for simbolo in lenguaje:
    print(simbolo + "\t", end="|")
print()
x = 0
for estado in tablaEstadosAFD:
    print(estado + "\t", end="|")
    for simbolo in lenguaje:
        print(tablaTransicionesAFD[x] + "\t", end="|")
        x = x + 1
    print()
input("Presione enter para continuar...")

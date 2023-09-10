from Nodo import Nodo
from ListaSimple import ListaSimple

class Tablero(Nodo):
    def __init__(self, nombre, fila, columna):
        super().__init__()
        self.nombre = nombre
        self.fila = fila 
        self.columna = columna
        self.piezas = ListaSimple()

    def imprimir(self):
        print(f'Tablero: {self.nombre}')
        self.piezas.mostrar()

    def cosultarFila(self):
        fila = self.fila
        return fila
    
    def cosultarColumna(self):
        columna = self.columna
        return columna

    def consultarPieza(self):
        pieza = self.piezas
        return pieza

    def get_item(self, fila, columna):
        actual = self.items.inicio
        while actual:
            if actual.fila == fila and actual.columna == columna:
                return actual
            actual = actual.siguiente
        return None
    
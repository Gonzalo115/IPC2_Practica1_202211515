from Nodo import Nodo
from ListaSimple import ListaSimple

class Tablero(Nodo):
    def __init__(self, id, fila, columna):
        super().__init__()
        self.id = id
        self.fila = fila 
        self.columna = columna
        self.piezas = ListaSimple()

    def imprimir(self):
        print(f'Tablero: {self.id}')
        self.piezas.mostrar()

    def get_item(self, fila, columna):
        actual = self.items.inicio
        while actual:
            if actual.fila == fila and actual.columna == columna:
                return actual
            actual = actual.siguiente
        return None
    
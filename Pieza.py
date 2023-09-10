from Nodo import Nodo

class Pieza(Nodo):

    def __init__(self, fila, columna, inicialColor, color):
        super().__init__()
        self.fila = fila
        self.columna = columna
        self.inicialColor = inicialColor
        self.color = color 


    def imprimir(self):
        print(f'[{self.inicialColor}]')
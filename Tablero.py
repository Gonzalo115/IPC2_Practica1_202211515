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

    def to_dot(self):
        # Nodo principal del elemento
        nodo_nombre = f'senales_{self.nombre}'
        cadena = f'"{nodo_nombre}" [label="Colorealo", shape=ellipse, color=black];\n'
        


        # Nodos para los items
        nodo_items = f'senales_{self.nombre}'

        # recorriendo los items
        for c in range(1, self.columna + 1):
            prev_item = nodo_items
            for r in range(1, self.fila + 1):
                pieza = self.get_item(r, c)
                item_nodo_id = f"{nodo_nombre}_item_{r}_{c}"

                if pieza:
                    cadena += f'"{item_nodo_id}" [label="{" " if pieza else " "}", shape=ellipse,color={pieza.color},style=filled,fillcolor={pieza.color}];\n'
                else:
                    cadena += f'"{item_nodo_id}" [label="{" " if pieza else " "}", shape=ellipse, color=black];\n'
                
                # Conectando el nodo "Items" solo a los items de la primera fila
                if r == 1:
                    cadena += f'"{nodo_items}" -> "{item_nodo_id}";\n'
                
                # Conectando los demás items
                else:
                    cadena += f'"{prev_item}" -> "{item_nodo_id}";\n'
                    
                prev_item = item_nodo_id
        return cadena

    def get_item(self, fila, columna):
        actual = self.piezas.inicio
        while actual:
            if actual.fila == fila and actual.columna == columna:
                return actual
            actual = actual.siguiente
        return None
    
    def tableroOrdenada(self):
        for r in range(1, self.fila + 1):
            for c in range (1, self.columna + 1):
                dato = self.get_item(r, c)
                if dato:
                    print(f'[{dato.inicialColor}]', end="\t")
                else:
                    print("[ ]", end="\t")
            print()
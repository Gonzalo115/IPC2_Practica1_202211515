class ListaSimple:
    def __init__(self):
        self.inicio = None
        
    def agregar_al_final(self, data):
        if self.inicio == None:
            self.inicio = data
        else: 
            #actual va ser nuestro inicio
            actual = self.inicio
            #vamos a buscar cuando el actual.siguiente sea igual null
            #es decir, el final de la lista 
            while actual.siguiente != None:
                actual = actual.siguiente 
            #insertar en el final de la lista 
            actual.siguiente = data
    
    def mostrar(self):
        actual = self.inicio
        while actual != None:
            actual.imprimir()
            actual = actual.siguiente 
        print("------------")
        
    def buscar_nombre(self, nombre):
        actual = self.inicio
        while actual != None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None
    
    def inicializar(self):
        if self.inicio != None:
            actual = self.inicio
            while actual.siguiente != None:
                actual = actual.siguiente
            self.inicio = None
            actual.siguiente = None

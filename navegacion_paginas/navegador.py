class Navegador:
    def __init__(self):
        # Pila de historial hacia atras
        self.pila_atras = []
        # Pila de historial hacia adelante
        self.pila_adelante = []
        self.pagina_actual = None

    def visitar(self, pagina):
        # PUSH: la pagina actual pasa a la pila de atras
        if self.pagina_actual:
            self.pila_atras.append(self.pagina_actual)
        self.pagina_actual = pagina
        # Al visitar una nueva pagina se borra el historial adelante
        self.pila_adelante.clear()
        print(f"Visitando: {self.pagina_actual.url}")

    def atras(self):
        if self.pila_atras:
            # POP de pila_atras, PUSH a pila_adelante
            self.pila_adelante.append(self.pagina_actual)
            self.pagina_actual = self.pila_atras.pop()
            print(f"Atras -> {self.pagina_actual.url}")
        else:
            print("No hay paginas anteriores")

    def adelante(self):
        if self.pila_adelante:
            # POP de pila_adelante, PUSH a pila_atras
            self.pila_atras.append(self.pagina_actual)
            self.pagina_actual = self.pila_adelante.pop()
            print(f"Adelante -> {self.pagina_actual.url}")
        else:
            print("No hay paginas siguientes")

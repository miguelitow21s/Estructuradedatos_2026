class Navegador:
    def __init__(self):
        # Pila de historial hacia atras
        self.pila_atras = []
        # Pila de historial hacia adelante
        self.pila_adelante = []
        self.pagina_actual = None

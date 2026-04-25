from collections import deque

class Impresora:
    def __init__(self):
        # Cola: documentos pendientes de imprimir (FIFO)
        self.cola_pendientes = deque()
        # Pila: documentos ya impresos (LIFO - para reimpresion)
        self.pila_impresos = []

from collections import deque

class Impresora:
    def __init__(self):
        # Cola: documentos pendientes de imprimir (FIFO)
        self.cola_pendientes = deque()
        # Pila: documentos ya impresos (LIFO - para reimpresion)
        self.pila_impresos = []

    def agregar_documento(self, documento):
        # ENQUEUE: entra al final de la cola de pendientes
        self.cola_pendientes.append(documento)
        print(f"Documento '{documento.nombre}' agregado a la cola de impresion")

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

    def imprimir_siguiente(self):
        if self.cola_pendientes:
            # DEQUEUE: sale el primero de la cola (FIFO)
            documento = self.cola_pendientes.popleft()
            # PUSH: se guarda en la pila de impresos (LIFO)
            self.pila_impresos.append(documento)
            print(f"Imprimiendo: '{documento.nombre}'")
        else:
            print("No hay documentos pendientes")

    def reimprimir_ultimo(self):
        if self.pila_impresos:
            # POP: se saca el ultimo impreso de la pila
            documento = self.pila_impresos.pop()
            print(f"Reimprimiendo: '{documento.nombre}'")
            # Vuelve a la pila despues de reimprimir
            self.pila_impresos.append(documento)
        else:
            print("No hay documentos impresos para reimprimir")

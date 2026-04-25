from collections import deque

class Clinica:
    def __init__(self):
        self.colas = {}  # {doctor: cola}
        self.turnos = []

    def agregar_doctor(self, doctor):
        self.colas[doctor] = deque()

    def agregar_paciente(self, doctor, paciente):
        # ENQUEUE: se agrega al final de la cola
        self.colas[doctor].append(paciente)
        print(f"{paciente.nombre} entra a la cola del Dr. {doctor.nombre}")

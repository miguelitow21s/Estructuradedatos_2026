from collections import deque

class Clinica:
    def __init__(self):
        self.colas = {}  # {doctor: cola}
        self.turnos = []

    def agregar_doctor(self, doctor):
        self.colas[doctor] = deque()

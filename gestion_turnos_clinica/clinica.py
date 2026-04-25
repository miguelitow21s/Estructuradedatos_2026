from collections import deque
from turno import Turno

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

    def atender_paciente(self, doctor):
        if doctor.disponible and self.colas[doctor]:
            # DEQUEUE: se saca el primer paciente
            paciente = self.colas[doctor].popleft()

            doctor.disponible = False

            turno = Turno(paciente, doctor)
            self.turnos.append(turno)

            turno.mostrar()

            doctor.disponible = True
        else:
            print(f"No hay pacientes o el Dr. {doctor.nombre} no está disponible")

class Turno:
    def __init__(self, paciente, doctor):
        self.paciente = paciente
        self.doctor = doctor

    def mostrar(self):
        print(f"Turno: {self.paciente.nombre} atendido por Dr. {self.doctor.nombre}")

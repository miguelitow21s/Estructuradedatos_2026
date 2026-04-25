from paciente import Paciente
from doctor import Doctor
from clinica import Clinica

# Crear clinica
clinica = Clinica()

# Crear doctores
doc1 = Doctor("Gomez")

clinica.agregar_doctor(doc1)

# Crear pacientes
p1 = Paciente("Ana")
p2 = Paciente("Luis")
p3 = Paciente("Carlos")

# Encolar pacientes
clinica.agregar_paciente(doc1, p1)
clinica.agregar_paciente(doc1, p2)
clinica.agregar_paciente(doc1, p3)

# Atender pacientes
clinica.atender_paciente(doc1)
clinica.atender_paciente(doc1)
clinica.atender_paciente(doc1)

# Sistema de Gestion de Turnos - Clinica

## Descripcion
Sistema que simula la atencion de pacientes en una clinica usando **colas (FIFO)**.
Cada doctor tiene su propia cola de pacientes. El primero en llegar es el primero en ser atendido.

## Estructura del proyecto

```
gestion_turnos_clinica/
├── paciente.py   # Clase Paciente
├── doctor.py     # Clase Doctor con estado de disponibilidad
├── turno.py      # Clase Turno que registra cada atencion
├── clinica.py    # Logica principal: colas por doctor
└── main.py       # Simulacion del sistema
```

## Clases

### Paciente (`paciente.py`)
- `nombre`: nombre del paciente

### Doctor (`doctor.py`)
- `nombre`: nombre del doctor
- `disponible`: booleano que indica si puede atender

### Turno (`turno.py`)
- `paciente`: paciente atendido
- `doctor`: doctor que lo atendio
- `mostrar()`: imprime el turno

### Clinica (`clinica.py`)
- `colas`: diccionario `{doctor: deque}` — una cola por doctor
- `turnos`: lista de turnos registrados
- `agregar_doctor(doctor)`: crea una cola vacia para el doctor
- `agregar_paciente(doctor, paciente)`: **ENQUEUE** — agrega al final de la cola
- `atender_paciente(doctor)`: **DEQUEUE** — saca el primero de la cola y genera un turno

## Operaciones de cola usadas

| Operacion | Metodo Python | Descripcion |
|-----------|---------------|-------------|
| Enqueue   | `append()`    | Paciente entra al final de la cola |
| Dequeue   | `popleft()`   | Primer paciente sale para ser atendido |

## Estructura de datos
Se usa `collections.deque` porque `append()` y `popleft()` son O(1).

## Como ejecutar

```bash
cd gestion_turnos_clinica
python main.py
```

## Salida esperada

```
Ana entra a la cola del Dr. Gomez
Luis entra a la cola del Dr. Gomez
Carlos entra a la cola del Dr. Gomez
Turno: Ana atendido por Dr. Gomez
Turno: Luis atendido por Dr. Gomez
Turno: Carlos atendido por Dr. Gomez
```

## Concepto clave
FIFO (First In, First Out): el primer paciente en llegar es el primero en ser atendido.

# Sistema de Impresion - Pilas y Colas

## Descripcion
Sistema que simula una impresora usando **cola (FIFO)** para los documentos pendientes
y **pila (LIFO)** para el historial de documentos impresos. Permite reimprimir el ultimo impreso.

## Estructura del proyecto

```
sistema_impresion/
├── documento.py   # Clase Documento con nombre
├── impresora.py   # Cola de pendientes + pila de impresos
└── main.py        # Simulacion del sistema
```

## Clases

### Documento (`documento.py`)
- `nombre`: nombre del archivo a imprimir

### Impresora (`impresora.py`)
- `cola_pendientes`: deque con documentos esperando ser impresos (FIFO)
- `pila_impresos`: lista con documentos ya impresos (LIFO)
- `agregar_documento(doc)`: **ENQUEUE** — agrega al final de la cola
- `imprimir_siguiente()`: **DEQUEUE + PUSH** — imprime el primero de la cola y lo guarda en la pila
- `reimprimir_ultimo()`: **POP** — vuelve a imprimir el ultimo documento de la pila

## Operaciones usadas

| Operacion | Estructura | Metodo Python | Descripcion |
|-----------|------------|---------------|-------------|
| Enqueue   | Cola       | `append()`    | Documento entra a la cola de espera |
| Dequeue   | Cola       | `popleft()`   | Primer documento sale a imprimir |
| Push      | Pila       | `append()`    | Documento impreso se guarda en historial |
| Pop       | Pila       | `pop()`       | Se recupera el ultimo impreso para reimprimir |

## Flujo del sistema

```
[Nuevo documento] --> cola_pendientes (FIFO)
                            |
                       imprimir_siguiente()
                            |
                     pila_impresos (LIFO)
                            |
                     reimprimir_ultimo()
```

## Como ejecutar

```bash
cd sistema_impresion
python main.py
```

## Salida esperada

```
Documento 'Informe.pdf' agregado a la cola de impresion
Documento 'Tarea.docx' agregado a la cola de impresion
Documento 'Foto.png' agregado a la cola de impresion
Imprimiendo: 'Informe.pdf'
Imprimiendo: 'Tarea.docx'
Reimprimiendo: 'Tarea.docx'
Imprimiendo: 'Foto.png'
No hay documentos pendientes
```

## Concepto clave
La **cola** garantiza orden justo (el primero en llegar, primero en imprimir).
La **pila** guarda el historial y permite recuperar el ultimo impreso rapidamente.

# Navegacion de Paginas - Pilas

## Descripcion
Sistema que simula el boton de atras y adelante de un navegador web usando **pilas (LIFO)**.
Dos pilas controlan el historial: una para retroceder y otra para avanzar.

## Estructura del proyecto

```
navegacion_paginas/
├── pagina.py      # Clase Pagina con URL
├── navegador.py   # Logica con dos pilas: pila_atras y pila_adelante
└── main.py        # Simulacion de navegacion
```

## Clases

### Pagina (`pagina.py`)
- `url`: direccion de la pagina

### Navegador (`navegador.py`)
- `pila_atras`: historial de paginas anteriores
- `pila_adelante`: historial de paginas siguientes
- `pagina_actual`: pagina que se esta viendo ahora
- `visitar(pagina)`: navega a una nueva pagina
- `atras()`: retrocede una pagina
- `adelante()`: avanza una pagina

## Operaciones de pila usadas

| Operacion | Metodo Python | Cuando ocurre |
|-----------|---------------|---------------|
| Push      | `append()`    | Al visitar, retroceder o avanzar |
| Pop       | `pop()`       | Al retroceder (pila_atras) o avanzar (pila_adelante) |

## Logica de navegacion

### Visitar nueva pagina
- La pagina actual hace PUSH a `pila_atras`
- `pila_adelante` se limpia (ya no hay "siguiente")

### Retroceder
- La pagina actual hace PUSH a `pila_adelante`
- POP de `pila_atras` → nueva pagina actual

### Avanzar
- La pagina actual hace PUSH a `pila_atras`
- POP de `pila_adelante` → nueva pagina actual

## Como ejecutar

```bash
cd navegacion_paginas
python main.py
```

## Salida esperada

```
Visitando: google.com
Visitando: youtube.com
Visitando: github.com
Atras -> youtube.com
Atras -> google.com
Adelante -> youtube.com
Adelante -> github.com
No hay paginas siguientes
```

## Concepto clave
LIFO (Last In, First Out): la ultima pagina visitada es la primera en recuperarse al retroceder.

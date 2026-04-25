from documento import Documento
from impresora import Impresora

impresora = Impresora()

# Agregar documentos a la cola (enqueue)
impresora.agregar_documento(Documento("Informe.pdf"))
impresora.agregar_documento(Documento("Tarea.docx"))
impresora.agregar_documento(Documento("Foto.png"))

# Imprimir en orden FIFO (dequeue + push a pila)
impresora.imprimir_siguiente()  # Informe.pdf
impresora.imprimir_siguiente()  # Tarea.docx

# Reimprimir el ultimo impreso usando la pila (pop)
impresora.reimprimir_ultimo()   # Tarea.docx

# Imprimir el restante
impresora.imprimir_siguiente()  # Foto.png

# Intentar imprimir sin pendientes
impresora.imprimir_siguiente()  # cola vacia

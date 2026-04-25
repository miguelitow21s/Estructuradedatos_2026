import tkinter as tk
from tkinter import messagebox
from documento import Documento
from impresora import Impresora

# ---------- DATOS ----------
impresora = Impresora()

# ---------- COLORES ----------
BG     = "#1e1e2e"
PANEL  = "#2a2a3d"
AZUL   = "#4f8ef7"
VERDE  = "#a6e3a1"
AMARILLO = "#f9e2af"
TEXTO  = "#cdd6f4"
GRIS   = "#45475a"

def actualizar_ui():
    # Cola de pendientes
    lista_cola.delete(0, tk.END)
    for i, doc in enumerate(impresora.cola_pendientes, 1):
        lista_cola.insert(tk.END, f"  {i}.  {doc.nombre}")
    lbl_cola.config(text=f"{len(impresora.cola_pendientes)} pendiente(s)")

    # Pila de impresos
    lista_pila.delete(0, tk.END)
    for doc in reversed(impresora.pila_impresos):
        lista_pila.insert(tk.END, f"  ✓  {doc.nombre}")
    lbl_pila.config(text=f"{len(impresora.pila_impresos)} impreso(s)")

    # Botones activos segun estado
    btn_imprimir.config(state=tk.NORMAL if impresora.cola_pendientes else tk.DISABLED)
    btn_reimprimir.config(state=tk.NORMAL if impresora.pila_impresos else tk.DISABLED)

def agregar():
    nombre = entry_doc.get().strip()
    if not nombre:
        messagebox.showwarning("Aviso", "Escribe el nombre del documento")
        return
    impresora.agregar_documento(Documento(nombre))
    entry_doc.delete(0, tk.END)
    actualizar_ui()

def imprimir():
    impresora.imprimir_siguiente()
    actualizar_ui()

def reimprimir():
    impresora.reimprimir_ultimo()
    actualizar_ui()

# ---------- VENTANA ----------
root = tk.Tk()
root.title("Sistema de Impresion")
root.resizable(False, False)
root.configure(bg=BG)

tk.Label(root, text="🖨️  Sistema de Impresion", font=("Arial", 15, "bold"),
         bg=BG, fg=AZUL, pady=12).pack()

# ---- Input nuevo documento ----
frame_input = tk.Frame(root, bg=BG, padx=16)
frame_input.pack(fill=tk.X)

tk.Label(frame_input, text="Documento:", font=("Arial", 10),
         bg=BG, fg=TEXTO).pack(side=tk.LEFT, padx=(0, 6))

entry_doc = tk.Entry(frame_input, font=("Arial", 12), bg=PANEL, fg=TEXTO,
                     insertbackground=TEXTO, relief=tk.FLAT, bd=6, width=28)
entry_doc.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry_doc.bind("<Return>", lambda _: agregar())

tk.Button(frame_input, text="Agregar a cola", font=("Arial", 10, "bold"),
          bg=AMARILLO, fg=BG, relief=tk.FLAT, cursor="hand2",
          padx=10, pady=4, activebackground=GRIS,
          command=agregar).pack(side=tk.LEFT, padx=(8, 0))

tk.Frame(root, bg=BG, height=8).pack()

# ---- Paneles cola / pila ----
frame_paneles = tk.Frame(root, bg=BG, padx=16)
frame_paneles.pack(fill=tk.BOTH, expand=True)

# Panel cola pendientes
col_cola = tk.Frame(frame_paneles, bg=PANEL)
col_cola.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

tk.Label(col_cola, text="Cola de pendientes (FIFO)", font=("Arial", 10, "bold"),
         bg=PANEL, fg=AMARILLO, pady=8).pack()

lista_cola = tk.Listbox(col_cola, font=("Arial", 11), bg=BG, fg=TEXTO,
                        selectbackground=AZUL, relief=tk.FLAT,
                        highlightthickness=0, height=7, bd=0)
lista_cola.pack(fill=tk.X, padx=10)

lbl_cola = tk.Label(col_cola, text="0 pendiente(s)", font=("Arial", 8),
                    bg=PANEL, fg=GRIS, pady=4)
lbl_cola.pack()

# Panel pila impresos
col_pila = tk.Frame(frame_paneles, bg=PANEL)
col_pila.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tk.Label(col_pila, text="Pila de impresos (LIFO)", font=("Arial", 10, "bold"),
         bg=PANEL, fg=VERDE, pady=8).pack()

lista_pila = tk.Listbox(col_pila, font=("Arial", 11), bg=BG, fg=VERDE,
                        selectbackground=AZUL, relief=tk.FLAT,
                        highlightthickness=0, height=7, bd=0)
lista_pila.pack(fill=tk.X, padx=10)

lbl_pila = tk.Label(col_pila, text="0 impreso(s)", font=("Arial", 8),
                    bg=PANEL, fg=GRIS, pady=4)
lbl_pila.pack()

# ---- Botones de accion ----
frame_btns = tk.Frame(root, bg=BG, pady=12, padx=16)
frame_btns.pack(fill=tk.X)

btn_imprimir = tk.Button(frame_btns, text="▶  Imprimir siguiente", font=("Arial", 11, "bold"),
                         bg=AZUL, fg="white", relief=tk.FLAT, cursor="hand2",
                         pady=6, activebackground="#3a6fd8", state=tk.DISABLED,
                         command=imprimir)
btn_imprimir.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))

btn_reimprimir = tk.Button(frame_btns, text="↩  Reimprimir ultimo", font=("Arial", 11, "bold"),
                           bg=VERDE, fg=BG, relief=tk.FLAT, cursor="hand2",
                           pady=6, activebackground="#7dc47a", state=tk.DISABLED,
                           command=reimprimir)
btn_reimprimir.pack(side=tk.LEFT, fill=tk.X, expand=True)

tk.Frame(root, bg=BG, height=4).pack()
root.mainloop()

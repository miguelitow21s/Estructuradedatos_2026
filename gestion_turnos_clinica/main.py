import tkinter as tk
from tkinter import messagebox
from paciente import Paciente
from doctor import Doctor
from clinica import Clinica

# ---------- DATOS ----------
clinica = Clinica()
doc1 = Doctor("Gomez")
doc2 = Doctor("Lopez")
clinica.agregar_doctor(doc1)
clinica.agregar_doctor(doc2)

# ---------- COLORES ----------
BG    = "#1e1e2e"
PANEL = "#2a2a3d"
VERDE = "#a6e3a1"
AZUL  = "#4f8ef7"
ROJO  = "#f38ba8"
TEXTO = "#cdd6f4"
GRIS  = "#45475a"
AMARILLO = "#f9e2af"

def actualizar_ui():
    for doc, (lista_cola, lista_turnos, lbl_count) in paneles.items():
        lista_cola.delete(0, tk.END)
        for i, p in enumerate(clinica.colas[doc], 1):
            lista_cola.insert(tk.END, f"  {i}.  {p.nombre}")

        lista_turnos.delete(0, tk.END)
        atendidos = [t for t in clinica.turnos if t.doctor == doc]
        for t in reversed(atendidos):
            lista_turnos.insert(tk.END, f"  ✓  {t.paciente.nombre}")

        total = len(clinica.colas[doc])
        lbl_count.config(text=f"{total} en cola")

def agregar(doctor):
    nombre = entries[doctor].get().strip()
    if not nombre:
        messagebox.showwarning("Aviso", "Escribe el nombre del paciente")
        return
    clinica.agregar_paciente(doctor, Paciente(nombre))
    entries[doctor].delete(0, tk.END)
    actualizar_ui()

def atender(doctor):
    if not clinica.colas[doctor]:
        messagebox.showinfo("Cola vacia", f"No hay pacientes para el Dr. {doctor.nombre}")
        return
    clinica.atender_paciente(doctor)
    actualizar_ui()

# ---------- VENTANA ----------
root = tk.Tk()
root.title("Clinica - Sistema de Turnos")
root.resizable(False, False)
root.configure(bg=BG)

tk.Label(root, text="🏥  Sistema de Turnos", font=("Arial", 15, "bold"),
         bg=BG, fg=AZUL, pady=12).pack()

frame_doctores = tk.Frame(root, bg=BG)
frame_doctores.pack(padx=16, pady=(0, 12))

paneles = {}
entries = {}

for doc, color_btn in [(doc1, VERDE), (doc2, AMARILLO)]:
    col = tk.Frame(frame_doctores, bg=PANEL, bd=0, relief=tk.FLAT)
    col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8)

    tk.Label(col, text=f"Dr. {doc.nombre}", font=("Arial", 12, "bold"),
             bg=PANEL, fg=color_btn, pady=8).pack()

    # Input agregar
    frame_input = tk.Frame(col, bg=PANEL)
    frame_input.pack(padx=10, fill=tk.X)

    entry = tk.Entry(frame_input, font=("Arial", 11), bg=BG, fg=TEXTO,
                     insertbackground=TEXTO, relief=tk.FLAT, bd=6)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    entry.bind("<Return>", lambda _, d=doc: agregar(d))
    entries[doc] = entry

    tk.Button(frame_input, text="+", font=("Arial", 12, "bold"),
              bg=color_btn, fg=BG, relief=tk.FLAT, cursor="hand2",
              padx=8, activebackground=GRIS,
              command=lambda d=doc: agregar(d)).pack(side=tk.LEFT, padx=(6, 0))

    tk.Frame(col, bg=PANEL, height=8).pack()

    # Cola
    tk.Label(col, text="Cola de espera (FIFO)", font=("Arial", 9),
             bg=PANEL, fg=GRIS).pack()

    lista_cola = tk.Listbox(col, font=("Arial", 11), bg=BG, fg=TEXTO,
                            selectbackground=AZUL, relief=tk.FLAT,
                            highlightthickness=0, height=5, bd=0)
    lista_cola.pack(fill=tk.X, padx=10, pady=(2, 0))

    lbl_count = tk.Label(col, text="0 en cola", font=("Arial", 8),
                         bg=PANEL, fg=GRIS)
    lbl_count.pack()

    # Boton atender
    tk.Button(col, text="Atender siguiente →", font=("Arial", 10, "bold"),
              bg=AZUL, fg="white", relief=tk.FLAT, cursor="hand2",
              pady=5, activebackground="#3a6fd8",
              command=lambda d=doc: atender(d)).pack(fill=tk.X, padx=10, pady=8)

    # Turnos atendidos
    tk.Label(col, text="Atendidos", font=("Arial", 9),
             bg=PANEL, fg=GRIS).pack()

    lista_turnos = tk.Listbox(col, font=("Arial", 11), bg=BG, fg=VERDE,
                              selectbackground=AZUL, relief=tk.FLAT,
                              highlightthickness=0, height=4, bd=0)
    lista_turnos.pack(fill=tk.X, padx=10, pady=(2, 10))

    paneles[doc] = (lista_cola, lista_turnos, lbl_count)

tk.Frame(root, bg=BG, height=8).pack()
root.mainloop()

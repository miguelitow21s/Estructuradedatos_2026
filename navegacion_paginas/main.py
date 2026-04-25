import tkinter as tk
from tkinter import messagebox
from pagina import Pagina
from navegador import Navegador

nav = Navegador()

def actualizar_ui():
    # Barra de URL
    url_actual = nav.pagina_actual.url if nav.pagina_actual else ""
    entry_url.delete(0, tk.END)
    entry_url.insert(0, url_actual)

    # Botones atras/adelante
    btn_atras.config(state=tk.NORMAL if nav.pila_atras else tk.DISABLED)
    btn_adelante.config(state=tk.NORMAL if nav.pila_adelante else tk.DISABLED)

    # Pila atras
    lista_atras.delete(0, tk.END)
    for p in reversed(nav.pila_atras):
        lista_atras.insert(tk.END, p.url)

    # Pila adelante
    lista_adelante.delete(0, tk.END)
    for p in reversed(nav.pila_adelante):
        lista_adelante.insert(tk.END, p.url)

def visitar():
    url = entry_url.get().strip()
    if not url:
        messagebox.showwarning("Aviso", "Escribe una URL primero")
        return
    nav.visitar(Pagina(url))
    actualizar_ui()

def ir_atras():
    nav.atras()
    actualizar_ui()

def ir_adelante():
    nav.adelante()
    actualizar_ui()

# ---------- VENTANA ----------
root = tk.Tk()
root.title("Navegador - Pilas")
root.resizable(False, False)

BG = "#1e1e2e"
PANEL = "#2a2a3d"
AZUL = "#4f8ef7"
TEXTO = "#cdd6f4"
GRIS = "#45475a"

root.configure(bg=BG)

# ---- Barra superior ----
frame_top = tk.Frame(root, bg=BG, pady=8, padx=12)
frame_top.pack(fill=tk.X)

btn_atras = tk.Button(frame_top, text="←", width=3, font=("Arial", 14, "bold"),
                      bg=PANEL, fg=TEXTO, relief=tk.FLAT, cursor="hand2",
                      activebackground=GRIS, command=ir_atras, state=tk.DISABLED)
btn_atras.pack(side=tk.LEFT, padx=(0, 4))

btn_adelante = tk.Button(frame_top, text="→", width=3, font=("Arial", 14, "bold"),
                         bg=PANEL, fg=TEXTO, relief=tk.FLAT, cursor="hand2",
                         activebackground=GRIS, command=ir_adelante, state=tk.DISABLED)
btn_adelante.pack(side=tk.LEFT, padx=(0, 8))

entry_url = tk.Entry(frame_top, font=("Arial", 12), bg=PANEL, fg=TEXTO,
                     insertbackground=TEXTO, relief=tk.FLAT, bd=6)
entry_url.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry_url.insert(0, "google.com")
entry_url.bind("<Return>", lambda e: visitar())

btn_ir = tk.Button(frame_top, text="Ir", font=("Arial", 11, "bold"),
                   bg=AZUL, fg="white", relief=tk.FLAT, cursor="hand2",
                   padx=10, activebackground="#3a6fd8", command=visitar)
btn_ir.pack(side=tk.LEFT, padx=(8, 0))

# ---- Pilas ----
frame_pilas = tk.Frame(root, bg=BG, padx=12, pady=8)
frame_pilas.pack(fill=tk.BOTH, expand=True)

def panel_pila(parent, titulo):
    f = tk.Frame(parent, bg=PANEL, bd=0, relief=tk.FLAT)
    f.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=6)
    tk.Label(f, text=titulo, font=("Arial", 10, "bold"),
             bg=PANEL, fg=AZUL, pady=6).pack()
    lb = tk.Listbox(f, font=("Arial", 11), bg=PANEL, fg=TEXTO,
                    selectbackground=AZUL, relief=tk.FLAT,
                    highlightthickness=0, height=8, bd=0)
    lb.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
    return lb

lista_atras    = panel_pila(frame_pilas, "⬅  pila_atras  (TOP → BOTTOM)")
lista_adelante = panel_pila(frame_pilas, "➡  pila_adelante  (TOP → BOTTOM)")

# ---- Paginas rapidas ----
frame_rapidas = tk.Frame(root, bg=BG, pady=6)
frame_rapidas.pack()

tk.Label(frame_rapidas, text="Accesos rapidos:", bg=BG, fg=GRIS,
         font=("Arial", 9)).pack(side=tk.LEFT, padx=(8, 6))

for sitio in ["google.com", "youtube.com", "github.com", "wikipedia.org"]:
    tk.Button(frame_rapidas, text=sitio, font=("Arial", 9),
              bg=PANEL, fg=TEXTO, relief=tk.FLAT, cursor="hand2",
              padx=6, activebackground=GRIS,
              command=lambda s=sitio: [entry_url.delete(0, tk.END),
                                       entry_url.insert(0, s), visitar()]
              ).pack(side=tk.LEFT, padx=3)

tk.Frame(root, bg=BG, height=8).pack()

root.mainloop()

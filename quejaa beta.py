import tkinter as tk
from tkinter import simpledialog, filedialog

def editar():
    nuevo_nombre = simpledialog.askstring("Editar nombre", "Nuevo nombre:")
    nueva_desc = simpledialog.askstring("Editar descripción", "Nueva descripción:")
    if nuevo_nombre:
        label_nombre.config(text=nuevo_nombre)
    if nueva_desc:
        label_desc.config(text=nueva_desc)
    nueva_img = filedialog.askopenfilename(
        title="Selecciona imagen",
        filetypes=[("Archivos PNG", "*.png"), ("Archivos GIF", "*.gif")]
    )
    if nueva_img:
        try:
            foto = tk.PhotoImage(file=nueva_img)
            label_img.config(image=foto)
            label_img.image = foto
        except Exception as e:
            label_img.config(text="No se pudo cargar la imagen", image="")
            label_img.image = None

root = tk.Tk()
root.title("Mi Página Personal")
root.geometry("400x350")
fuente = ("Arial", 14)

label_img = tk.Label(root)
label_img.pack(pady=10)
label_nombre = tk.Label(root, text="Tu Nombre", font=fuente)
label_nombre.pack()
label_desc = tk.Label(root, text="Descripción corta aquí.", font=fuente)
label_desc.pack(pady=10)
tk.Button(root, text="Editar", command=editar, font=fuente).pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

contactos = []

def actualizar_listbox():

    listbox_contactos.delete(0, tk.END)
    for c in contactos:
        listbox_contactos.insert(tk.END, f"{c['nombre']} - {c['teléfono']}")

def agregar_contacto():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    if nombre and telefono:
        contacto = {
            "nombre": nombre,
            "teléfono": telefono,
            "correo": correo if correo else "No reconocido como medio de contacto"
        }
        contactos.append(contacto)
        actualizar_listbox()
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
    else:
        messagebox.showwarning( "Nombre y Teléfono son obligatorios,pa.")

def ordenar_por_nombre():
    contactos.sort(key=lambda c: c["nombre"].lower())
    actualizar_listbox()

def ordenar_por_telefono():
    contactos.sort(key=lambda c: c["teléfono"])
    actualizar_listbox()

def buscar_contacto():
    nombre_buscado = entry_buscar.get().strip().lower()
    encontrados = [c for c in contactos if nombre_buscado in c["nombre"].lower()]
    listbox_contactos.delete(0, tk.END)
    for c in encontrados:
        listbox_contactos.insert(tk.END, f"{c['nombre']} - {c['teléfono']}")

def mostrar_todos():
    actualizar_listbox()

ventana = tk.Tk()
ventana.title("Mis Contactos")
ventana.configure(bg="white")
ventana.geometry("783x618")

fuente = ("Arial", 15)

tk.Label(ventana, text="Nombre/apodo:", bg="white", fg="black", font=fuente).pack(pady=3)
entry_nombre = tk.Entry(ventana, font=fuente, fg="black", bg="white", insertbackground="black")
entry_nombre.pack(pady=3)

tk.Label(ventana, text="Num.cel:", bg="white", fg="black", font=fuente).pack(pady=3)
entry_telefono = tk.Entry(ventana, font=fuente, fg="black", bg="white", insertbackground="black")
entry_telefono.pack(pady=3)

tk.Label(ventana, text="Correo:", bg="white", fg="black", font=fuente).pack(pady=3)
entry_correo = tk.Entry(ventana, font=fuente, fg="black", bg="white", insertbackground="black")
entry_correo.pack(pady=3)

tk.Button(ventana, text="Agregar Contac", command=agregar_contacto, bg="lightblue", fg="black", font=fuente).pack(pady=5)
tk.Button(ventana, text="Ordenar por Nombre/apodo (ABC)", command=ordenar_por_nombre, bg="lightyellow", fg="black", font=fuente).pack(pady=5)
tk.Button(ventana, text="Ordenar por cel", command=ordenar_por_telefono, bg="lightgreen", fg="black", font=fuente).pack(pady=5)

tk.Label(ventana, text="Buscar Nombre:", bg="white", fg="black", font=fuente).pack(pady=3)
entry_buscar = tk.Entry(ventana, font=fuente, fg="black", bg="white", insertbackground="black")
entry_buscar.pack(pady=3)
tk.Button(ventana, text="Busca contac", command=buscar_contacto, bg="lightgray", fg="black", font=fuente).pack(pady=5)
tk.Button(ventana, text="Mostrar Todos los contac", command=mostrar_todos, bg="lightgray", fg="black", font=fuente).pack(pady=5)

listbox_contactos = tk.Listbox(ventana, width=40, font=fuente, fg="black", bg="white")
listbox_contactos.pack(pady=10)

ventana.mainloop()
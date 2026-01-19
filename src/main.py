import tkinter as tk

def main():
    ventana = tk.Tk()
    ventana.title("Comprobador de Conectividad Web")
    ventana.geometry("400x200")
    ventana.resizable(False, False)

    etiqueta_url = tk.Label(ventana, text="Introduce la URL:")
    etiqueta_url.pack(pady=10)

    entrada_url = tk.Entry(ventana, width=50)
    entrada_url.pack()

    etiqueta_resultado = tk.Label(ventana, text="")
    etiqueta_resultado.pack(pady=15)

    ventana.mainloop()

if __name__ == "__main__":
    main()

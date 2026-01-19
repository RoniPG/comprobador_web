import tkinter as tk
from urllib.request import urlopen


def comprobar_web(entrada_url, etiqueta_resultado):
    """
    Comprueba si una URL es accesible y actualiza la etiqueta de resultado."""

    url = entrada_url.get().strip()

    if not url:
        etiqueta_resultado.config(text="Introduce una URL")
        return
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        response = urlopen(url=url)
        if response.getcode() == 200:
            etiqueta_resultado.config(text=" La web está disponible")
        else:
            etiqueta_resultado.config(text=" La web no está disponible")
    except:
        etiqueta_resultado.config(text=" Error al conectar")


def main():
    """
    Configura la interfaz gráfica y maneja la interacción del usuario.
    """
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

    tk.Button(ventana, text="Comprobar", command=lambda: comprobar_web(entrada_url, etiqueta_resultado)).pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()

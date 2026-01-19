import tkinter as tk
from urllib.request import urlopen


def comprobar_web(entrada_url, etiqueta_resultado, btn):
    """
    Comprueba si una URL es accesible y actualiza la etiqueta de resultado.
    """
    
    btn.config(state="disabled")
    url = entrada_url.get().strip()

    if not url:
        etiqueta_resultado.config(text="Introduce una URL")
        btn.config(state="normal")
        return
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        response = urlopen(url=url, timeout=5)
        if response.getcode() == 200:
            etiqueta_resultado.config(text=" La web está disponible", fg="green")
        else:
            etiqueta_resultado.config(text=" La web no está disponible", fg="red")
    except:
        etiqueta_resultado.config(text=" Tiempo de espera agotado", fg="orange")
    finally:
        btn.config(state="normal")

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

    btn_comprobar = tk.Button(ventana, text="Comprobar", command=lambda: comprobar_web(entrada_url, etiqueta_resultado, btn_comprobar))
    btn_comprobar.pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()

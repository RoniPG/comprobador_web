# :globe_with_meridians: Comprobador de conectividad web

Proyecto en Python con interfaz gráfica (Tkinter) para comprobar el estado de sitios web.

---

## 🎯 Objetivo del proyecto

- Permitir al usuario introducir una URL en una ventana gráfica.
- Informar al usuario si el sitio está disponible (código 200) o no.

---

## 🧠 Tecnologías utilizadas

- **Pytoh 3.11+**
- **tkinter** y **urlib** para la GUI

---

## 📂 Estructura del proyecto

```
comprobador_conectividad_web/
│
├── src/                 
│   └── main.py
│
├── .gitignore
├── README.md
```


---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.11 o superior** instalado.

1. 1  (Opcional) Crear un entorno virtual con conda

   ```
    conda create -n comprobador_web_env python=3.11
    conda activate comprobador_web_env
   ```

#### 2. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/comprobador_web.git
   ```

#### 3. Accede al directorio del proyecto:

   ```
    cd comprobador_web
   ```

---

## :rocket: Uso

Desde la raíz del proyecto, ejecuta:
   ```
    python src/main.py
   ```
Se abrirá una ventana con:

- Un campo de entrada para introducir la URL del sitio web
- Un botón para comprobar la conectividad
- Un label que informará si la web está disponible o no según el código HTTP recibido

---

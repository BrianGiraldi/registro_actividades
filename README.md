# Evaluacion Final Integradora 

Aplicacion de consola para llevar un registro semanal de actividades fisicas (caminatas, ciclismo, gimnasio, etc.).

## Archivos del proyecto
- `main.py`: archivo principal con el menu interactivo.
- `actividad.py`: contiene la clase `Actividad` y las funciones para registrar y listar.
- `utilidades.py`: contiene las validaciones con `try/except`, el manejo del archivo JSON, los calculos de promedio/totales, la busqueda con `filter` y `lambda`, y el grafico con `matplotlib`.
- `actividades.json`: archivo de datos con algunas actividades de ejemplo ya cargadas.
- `grafico_actividades.png`: captura del grafico de barras generado por el programa.
- `requirements.txt`: libreria externa utilizada.

## Como ejecutar el programa
1. Instalar la libreria necesaria desde la terminal:
   ```
   pip install -r requirements.txt
   ```
2. Ejecutar el archivo principal:
   ```
   python main.py
   ```

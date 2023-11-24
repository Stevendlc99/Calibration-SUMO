# Tutorial para la creación del dataset

## Escenario 2
El tutorial se realizá para el escenario 2 como base, la metodología propuesta puede ser aplicada a otros escenarios.
## Selección de las rutas
1. Utilizando NetEdit seleccionaremos el área que queremos calibrar y las posibles rutas que existan.
![Logo de mi proyecto](https://github.com/Stevendlc99/Calibration-SUMO/raw/main/Images/netedit.jpeg)
3. Una vez identificadas las rutas, procedemos a colocarlas en el archivo connection_SUMO.py de la siguiente manera:
![Logo de mi proyecto](https://github.com/Stevendlc99/Calibration-SUMO/raw/main/Images/rutas.jpeg)
5. Añadimos los contadores en las intersecciones o salidas y realizamos el conteo.
![Logo de mi proyecto](https://github.com/Stevendlc99/Calibration-SUMO/raw/main/Images/contadores.jpeg)
## Para ejecutar múltiples simulaciones

1. El archivo generator.py contiene la automatización para la ejecución de varias simulaciones, las probabilidades de ruta y el volúmen de vehículos.
2. En el ejemplo ejecutaremos una simulación para un volúmen de 1000 vehículos que serán distribuidos de manera aleatoria en las entradas de la red.
3. Las entradas se guardaran en el archivo Excel "entradas_simulador-normal" y las salidas (Conteos) en el archivo Excel "salidas-simulador-normal".
![Logo de mi proyecto](https://github.com/Stevendlc99/Calibration-SUMO/raw/main/Images/generador.jpeg)
## Si queremos utilizar la GUI de SUMO 
1. En el archivo IbarraTriangle.sumocfg debemos descomentar la línea route files.
![Logo de mi proyecto](https://github.com/Stevendlc99/Calibration-SUMO/raw/main/Images/rou.jpeg)
3. El archivo rutas_conrou.py tiene los mismos parámetros de entrada que conection_SUMO.py (volumen de vehículos, probabilidades de ruta), pero genera un archivo con extensión .rou.xml que es compatible con GUI de SUMO.

5. rutas_conrou.py tiene un ejemplo para su creación. 


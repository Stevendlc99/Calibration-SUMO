# Tutorial para la creación del dataset

## Escenario 2
El tutorial se realizá para el escenario 2 como base, la metodología propuesta puede ser aplicada a otros escenarios.
## Selección de las rutas
1. Utilizando NetEdit seleccionaremos el área que queremos calibrar y las posibles rutas que existan.

3. Una vez identificadas las rutas, procedemos a colocarlas en el archivo connection_SUMO.py.
4. Añadimos los contadores en las intersecciones o salidas.
## Para ejecutar múltiples simulaciones

1. El archivo generator.py contiene la automatización para la ejecución de varias simulaciones, las probabilidades de ruta y el volúmen de vehículos.
2. En el ejemplo ejecutaremos una simulación de 3600 segundos para un volúmen de 1000 vehículos que serán distribuidos de manera aleatoria en las entradas de la red. 


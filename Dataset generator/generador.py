from conection_SUMO import JTRrouter
from Excel_entradas import guardar_datos_excel
from Excel_entradas import guardar_datos_excel_salida
import random
import numpy as np

def generar_conjunto_probabilidades():
    conjunto = np.random.dirichlet(np.ones(4))
    while any(prob <= 0.1 for prob in conjunto):
        conjunto = np.random.dirichlet(np.ones(4))
    return conjunto

# Simulación para diferentes valores de volumen total de vehículos y probabilidades de ruta 
for volumen_total in range(0, 1000):
    # Generar los parámetros de entrada en cada iteración, se le dara un volúmen aleatorio a cada entrada de simulación
    volumen1 = random.randint(0, volumen_total) 
    volumen2 = random.randint(0, volumen_total - volumen1)
    volumen3 = random.randint(0, volumen_total - volumen1 - volumen2)
    volumen4 = volumen_total - volumen1 - volumen2 - volumen3
    
    probabilidades_rutas = generar_conjunto_probabilidades()
    
    # Guardar datos en excel
    guardar_datos_excel(volumen1, volumen2, volumen3, volumen4,
                                                probabilidades_rutas)
    # Llamar a la función de simulación con los parámetros actualizados
    resultado_simulacion = JTRrouter(volumen1, volumen2, volumen3, volumen4,
                                                probabilidades_rutas)
    guardar_datos_excel_salida(resultado_simulacion)
    

import traci
import random
import traci.exceptions as traci_ex
import traci



def JTRrouter(volumen1,volumen2,volumen3,volumen4,probabilidades_rutas):

    try:
        # Iniciar la conexión con SUMO
        traci.start(["sumo", "-c", "IbarraTriangle.sumocfg"])
        
        # Resto del código de tu función JTRrouter
        # ...
    
    except traci_ex.TraCIException:
        # Cerrar la conexión TraCI si se produce una excepción
        traci.close()
        # Iniciar una nueva conexión con SUMO
        traci.start(["sumo", "-c", "IbarraTriangle.sumocfg"])

    # Iniciar la conexión con SUMO
    #traci.start(["sumo", "-c", "IbarraTriangle.sumocfg"])

    # Definir las rutas posibles
    rutas = [
        ["d1", "u4", "j1", "j2"], 
        ["d1", "u4", "u5", "u6", "g1"], 
        ["d1", "u4", "u5", "u6", "u7", "e1"], 
        ["d1", "u4", "u5", "u6", "u7", "u1", "u2", "h1"]
    ]

    rutas2 = [
        ["b2", "b1", "u6", "u7", "u1", "u2", "u3", "u4", "j1", "j2"], 
        ["b2", "b1", "u6", "g1"], 
        ["b2", "b1", "u6", "u7", "e1"], 
        ["b2", "b1", "u6", "u7", "u1", "u2", "h1"]
    ]

    rutas3 = [
        ["a21", "u1", "u2", "u3", "u4", "j1", "j2"], 
        ["a21", "u1", "u2", "u3", "u4", "u5", "u6", "g1" ], 
        ["a21", "e1"], 
        ["a21", "u1", "u2", "h1"]
    ]
    rutas4 = [
        ["i1", "u2", "u3", "u4", "j1", "j2"], 
        ["i1", "u2", "u3", "u4", "u5", "u6", "g1" ], 
        ["i1", "u2", "u3", "u4", "u5", "u6", "u7", "e1"], 
        ["i1", "u2","h1"]
    ]

 
    # Contadores de salida
    contador_salida1 = 0
    contador_salida2 = 0
    contador_salida3 = 0
    contador_salida4 = 0
    # Lista para almacenar los IDs de los vehículos generados y sus rutas
    vehiculos_generados = []

    #Generacion de vehiculos para la-------------------------------- ruta 1---------------------------------------

    for i in range(volumen1):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        
        # Seleccionar una ruta aleatoriamente según las probabilidades
        route = random.choices(rutas, probabilidades_rutas)[0]
        
        traci.vehicle.add(vehicle_id, routeID="")
        traci.vehicle.setRoute(vehicle_id, route)
        vehiculos_generados.append((vehicle_id, route))


    #Generacion de vehiculos para la----------------------------------- ruta 2------------------------------------
    for i in range(volumen1,(volumen1+volumen2)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        
        # Seleccionar una ruta aleatoriamente según las probabilidades
        route = random.choices(rutas2, probabilidades_rutas)[0]
        
        traci.vehicle.add(vehicle_id, routeID="")
        traci.vehicle.setRoute(vehicle_id, route)
        vehiculos_generados.append((vehicle_id, route))

    #Generacion de vehiculos para la------------------------------------- ruta 3----------------------------------
    for i in range((volumen1+volumen2), (volumen1+volumen2+volumen3)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        
        # Seleccionar una ruta aleatoriamente según las probabilidades
        route = random.choices(rutas3, probabilidades_rutas)[0]
        
        traci.vehicle.add(vehicle_id, routeID="")
        traci.vehicle.setRoute(vehicle_id, route)
        vehiculos_generados.append((vehicle_id, route))

    #Generacion de vehiculos para la -----------------------------------ruta 4 --------------------------------

    for i in range((volumen1+volumen2+volumen3), (volumen1+volumen2+volumen3+ volumen4)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        
        # Seleccionar una ruta aleatoriamente según las probabilidades
        route = random.choices(rutas4, probabilidades_rutas)[0]
        
        traci.vehicle.add(vehicle_id, routeID="")
        traci.vehicle.setRoute(vehicle_id, route)
        vehiculos_generados.append((vehicle_id, route))

    for vehicle, route in vehiculos_generados:
            contador_salida1 += route.count('j2')
            contador_salida2 += route.count('e1')
            contador_salida3 += route.count('g1')
            contador_salida4 += route.count('h1')

    resultados = [contador_salida1, contador_salida2, contador_salida3, contador_salida4]

    # Cerrar la conexión con SUMO
    traci.close()

    # Devolver los resultados
    return resultados


#test=JTRrouter(10,20,30,40,[0.3,0.1,0.2,0.4])
#print(test)

import traci
import random
import traci.exceptions as traci_ex

def JTRrouter(volumen1, volumen2, volumen3, volumen4, probabilidades_rutas):
    try:
        # Iniciar la conexión con SUMO
        traci.start(["sumo", "-c", "IbarraTriangle.sumocfg"])

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
        contador_salida_j2 = 0
        contador_salida_e1 = 0
        contador_salida_g1 = 0
        contador_salida_h1 = 0

        # Generación de vehículos
        for i in range(volumen1):
            vehicle_id = f"vehicle{i}"
            route = random.choices(rutas, probabilidades_rutas, k=1)[0]
            traci.vehicle.add(vehicle_id, routeID=route[0])
            traci.vehicle.setRoute(vehicle_id, route)

        for i in range(volumen1, volumen1 + volumen2):
            vehicle_id = f"vehicle{i}"
            route = random.choices(rutas2, probabilidades_rutas, k=1)[0]
            traci.vehicle.add(vehicle_id, routeID=route[0])
            traci.vehicle.setRoute(vehicle_id, route)

        for i in range(volumen1 + volumen2, volumen1 + volumen2 + volumen3):
            vehicle_id = f"vehicle{i}"
            route = random.choices(rutas3, probabilidades_rutas, k=1)[0]
            traci.vehicle.add(vehicle_id, routeID=route[0])
            traci.vehicle.setRoute(vehicle_id, route)

        for i in range(volumen1 + volumen2 + volumen3, volumen1 + volumen2 + volumen3 + volumen4):
            vehicle_id = f"vehicle{i}"
            route = random.choices(rutas4, probabilidades_rutas, k=1)[0]
            traci.vehicle.add(vehicle_id, routeID=route[0])
            traci.vehicle.setRoute(vehicle_id, route)


        # Lista para almacenar los IDs de los vehículos que pasan por cada arista
        vehiculos_j2 = []
        vehiculos_e1 = []
        vehiculos_g1 = []
        vehiculos_h1 = []

        # Simulación
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()

            # Obtener el número de vehículos en cada salida
            vehiculos_j2 = traci.edge.getLastStepVehicleIDs("j2")
            contador_salida_j2 += len(vehiculos_j2)

            vehiculos_e1 = traci.edge.getLastStepVehicleIDs("e1")
            contador_salida_e1 += len(vehiculos_e1)

            vehiculos_g1 = traci.edge.getLastStepVehicleIDs("g1")
            contador_salida_g1 += len(vehiculos_g1)

            vehiculos_h1 = traci.edge.getLastStepVehicleIDs("h1")
            contador_salida_h1 += len(vehiculos_h1)



        # Cerrar la conexión con SUMO
        traci.close()

        return [contador_salida_j2, contador_salida_e1, contador_salida_g1, contador_salida_h1]

    except traci_ex.TraCIException:
        # Cerrar la conexión TraCI si se produce una excepción
        traci.close()
        # Iniciar una nueva conexión con SUMO
        traci.start(["sumo", "-c", "IbarraTriangle.sumocfg"])


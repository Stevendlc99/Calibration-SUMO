import traci
import random
import xml.etree.ElementTree as ET
def JTRrouter(volumen1,volumen2,volumen3,volumen4,probabilidades_rutas):
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


    # Generar el archivo .rou.xml
    root = ET.Element("routes")
    for i in range(volumen1):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        route = random.choices(rutas, probabilidades_rutas)[0]

        vehicle = ET.SubElement(root, "vehicle", id=vehicle_id, depart="0", departLane="best", departSpeed="0")
        ET.SubElement(vehicle, "route", edges=" ".join(route))

    for i in range(volumen1,(volumen1+volumen2)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        route = random.choices(rutas2, probabilidades_rutas)[0]

        vehicle = ET.SubElement(root, "vehicle", id=vehicle_id, depart="0", departLane="best", departSpeed="0")
        ET.SubElement(vehicle, "route", edges=" ".join(route))
    for i in range((volumen1+volumen2), (volumen1+volumen2+volumen3)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        route = random.choices(rutas3, probabilidades_rutas)[0]

        vehicle = ET.SubElement(root, "vehicle", id=vehicle_id, depart="0", departLane="best", departSpeed="0")
        ET.SubElement(vehicle, "route", edges=" ".join(route))
    for i in range((volumen1+volumen2+volumen3), (volumen1+volumen2+volumen3+ volumen4)):
        vehicle_id = f"vehicle{i}"  # Generar un ID único para cada vehículo
        route = random.choices(rutas4, probabilidades_rutas)[0]

        vehicle = ET.SubElement(root, "vehicle", id=vehicle_id, depart="0", departLane="best", departSpeed="0")
        ET.SubElement(vehicle, "route", edges=" ".join(route))

    tree = ET.ElementTree(root)
    tree.write("routes.rou.xml")


    # Simulación de un paso de tiempo
    traci.simulationStep()


    # Cerrar la conexión con SUMO
    traci.close()
    return 0

JTRrouter(191, 312, 103, 214, [0.2354184191567521, 0.14080024427271456, 0.14709059396233579, 0.47669074260819744])
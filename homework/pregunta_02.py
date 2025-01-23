"""Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    sequence = []
    with open("files/input/data.csv") as file:
        for line in file:
            sequence.append((line))
        sequence=[
            (value.strip().split("\t")) 
            for value in sequence
            ]
        order= sorted([(word, 1) for value in sequence for word in value[0]], key=lambda x: x[0]) 

    result={}
    for key, value in order:
        if key not in result.keys(): #Se suman los valores por letra para obtener la cantidad de repeticiones
            result[key]=0
        result [key] += value
    return list(result.items())

print(pregunta_02())

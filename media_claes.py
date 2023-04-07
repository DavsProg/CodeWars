def mejor_que_el_promedio(puntos_clase, tus_puntos):
    # Calcula el promedio sumando todos los puntos y dividiéndolos por el número de estudiantes, incluyéndote a ti.
    promedio = (sum(puntos_clase) + tus_puntos) / (len(puntos_clase) + 1)
    
    # Devuelve True si tu puntaje es mayor que el promedio, de lo contrario, devuelve False.
    return tus_puntos > promedio

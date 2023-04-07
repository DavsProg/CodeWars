def better_than_average(class_points, your_points):
    # Calcula el promedio sumando todos los puntos y dividiéndolos por el número de estudiantes, incluyéndote a ti.
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    
    # Devuelve True si tu puntaje es mayor que el promedio, de lo contrario, devuelve False.
    return your_points > average

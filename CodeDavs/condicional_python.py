# Definimos una función llamada personalized_greeting que toma dos parámetros: name y owner.
def personalized_greeting(name, owner):
    # Usamos una condición para comparar si el nombre es igual al propietario.
    if name == owner:
        # Si son iguales, devolvemos 'Hello boss'.
        return 'Hello boss'
    else:
        # Si no son iguales, devolvemos 'Hello guest'.
        return 'Hello guest'x 

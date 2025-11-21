# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
"""
items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}
"""

# sort_selection.py

items: list[int] = []
n: int = 0
i: int = 0        # Puntero a la posición actual a llenar con el mínimo
j: int = 0        # Puntero para buscar el mínimo en la porción no ordenada
min_idx: int = 0  # Índice del elemento mínimo encontrado hasta ahora

def init(vals: list[int]) -> None:
    """Inicializa el estado del algoritmo."""
    global items, n, i, j, min_idx
    items = list(vals)
    n = len(items)
    i = 0
    j = 1
    min_idx = 0 # min_idx siempre empieza en i, pero la búsqueda de min empieza en i+1 o j=1 para el primer paso.

def step() -> dict:
    """Realiza un solo micro-paso del Selection Sort."""
    global i, j, min_idx, items, n

    # Caso de finalización: i ha llegado al penúltimo elemento
    if i >= n - 1:
        return {"done": True}

    # La búsqueda del mínimo es desde i+1 hasta n-1.
    
    # 1. Búsqueda del Mínimo
    if j < n:
        # a) Comparar items[j] con items[min_idx]
        if items[j] < items[min_idx]:
            min_idx = j  # Actualizar el índice del mínimo
        
        a = j # Para la visualización
        b = min_idx # Para la visualización
        j += 1 # Mover el puntero de búsqueda
        
        return {"a": a, "b": b, "swap": False, "done": False}
        
    # 2. Intercambio y avance (cuando la búsqueda ha terminado, es decir, j == n)
    else:
        # Intercambiar el mínimo encontrado (en min_idx) con el elemento actual (en i)
        # Solo se hace swap si el mínimo no es el elemento en i
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            
            a = i
            b = min_idx
            
            # Resetear estado para la siguiente pasada 'i'
            i += 1
            min_idx = i
            j = i + 1
            
            return {"a": a, "b": b, "swap": True, "done": False}
        else:
            # No hay swap, solo avanzamos
            a = i
            b = min_idx

            # Resetear estado para la siguiente pasada 'i'
            i += 1
            min_idx = i
            j = i + 1
            
            return {"a": a, "b": b, "swap": False, "done": False}

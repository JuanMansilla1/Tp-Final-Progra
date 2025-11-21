# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
"""
items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    return {"done": True}
"""
# sort_insertion.py

items: list[int] = []
n: int = 0
i: int = 1  # Puntero para el elemento a insertar
j: int = 1  # Puntero para recorrer la porción ordenada

def init(vals: list[int]) -> None:
    """Inicializa el estado del algoritmo."""
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1 # El primer elemento (items[0]) ya se considera ordenado
    j = 1

def step() -> dict:
    """Realiza un solo micro-paso del Insertion Sort."""
    global i, j, items, n

    # Caso de finalización: i ha recorrido toda la lista
    if i >= n:
        return {"done": True}

    # El elemento a insertar es items[i]. 'j' retrocede para encontrar la posición.
    
    # 1. Recorrer hacia atrás y hacer swap
    # La porción ordenada es 0..j-1. Si j > 0 y items[j-1] > items[j], se hace swap
    if j > 0 and items[j - 1] > items[j]:
        # Swap requerido. Se realiza *antes* de devolver swap=True
        items[j], items[j - 1] = items[j - 1], items[j]
        
        a = j
        b = j - 1
        
        # Mover puntero 'j' hacia atrás
        j -= 1
        
        return {"a": a, "b": b, "swap": True, "done": False}
        
    # 2. Elemento insertado o ya ordenado. Avanzar a la siguiente pasada 'i'.
    else:
        # Si se llegó al inicio (j=0) o items[j-1] <= items[j] (encontró posición)
        
        # Resetear estado para la siguiente pasada 'i'
        i += 1
        j = i # 'j' comienza en la misma posición que 'i' para la siguiente iteración.
        
        # Devolvemos un paso de comparación simple (puede ser items[i-1] y items[i])
        if i < n:
             # Comparamos el último de la porción ordenada con el primero de la no ordenada
            a = i - 1 
            b = i
            return {"a": a, "b": b, "swap": False, "done": False}
        else:
             # Si i >= n, ya terminó
             return {"done": True}
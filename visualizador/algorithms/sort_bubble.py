# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

# sort_bubble.py

items: list[int] = []
n: int = 0
i: int = 0  # Contador de pasadas (elementos ya ordenados al final)
j: int = 0  # Puntero para la comparación adyacente

def init(vals: list[int]) -> None:
    """Inicializa el estado del algoritmo."""
    global items, n, i, j
    items = list(vals)  # Guardar copia
    n = len(items)
    i = 0
    j = 0

def step() -> dict:
    """Realiza un solo micro-paso del Bubble Sort."""
    global i, j, items, n

    # Caso de finalización: si i ha recorrido toda la lista
    if i >= n - 1:
        return {"done": True}

    # El rango de comparación disminuye con cada pasada 'i'
    # j+1 < n - i - 1 es el último índice válido para items[j+1]
    limit = n - i - 1

    # 1. Comparar items[j] y items[j+1]
    if items[j] > items[j + 1]:
        # Swap requerido. Se realiza *antes* de devolver swap=True
        items[j], items[j + 1] = items[j + 1], items[j]
        
        # Guardamos los índices para la UI
        a = j
        b = j + 1
        
        # 2. Mover puntero j para la siguiente comparación
        j += 1
        
        # 3. Verificar si la pasada 'i' ha terminado
        if j >= limit:
            i += 1
            j = 0
            
        return {"a": a, "b": b, "swap": True, "done": False}
    
    else:
        # No hay swap, solo comparación (la UI lo mostrará como un movimiento/comparación en 'a' y 'b')
        a = j
        b = j + 1

        # 2. Mover puntero j para la siguiente comparación
        j += 1

        # 3. Verificar si la pasada 'i' ha terminado
        if j >= limit:
            i += 1
            j = 0
            
        return {"a": a, "b": b, "swap": False, "done": False}

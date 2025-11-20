# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = [5,10,40,2,9,6,1,3,50,32,25,99,74,82,7,8,16,27,90,45]
i = 0 # CONTADOR
j = 0 # INDICE
n = len(items) 
swapCont = 0

def init(lista):
    copiaItems = items
    n = len(items) 
    i = 0 # Contador de pasadas
    j = 0 # Pos en cada pasada
    done = False # Si termino de ordenar
    swap = False # Intercambio
    swapCont = 0

def step():
    swap = False
    if items[j] > items[j+1]:
        items[j],items[j+1] = items[j+1],items[j]
        swap = True     
        swapCont += 1        
        return {"j": j, "j+1": j+1, "swap": swap, "done":False}
    j += 1
    if j+1 == n - i - 1:
        j = 0
        i += 1
    if i >= n - 1:
        return {"done": True}

from collections import deque

def sort_queue(queue):
    if len(queue) <= 1:
        return queue
    
    half = len(queue) // 2
    sublist1 = deque([queue[i] for i in range(half)])
    sublist2 = deque([queue[i] for i in range(half, len(queue))])

    queue1 = deque(sort_queue(sublist1))
    queue2 = deque(sort_queue(sublist2))

    final_queue = deque()
    while queue1 and queue2:
        if queue1[0] < queue2[0]:
            final_queue.append(queue1.popleft())
        else:
            final_queue.append(queue2.popleft())
    final_queue.extend(queue1)
    final_queue.extend(queue2)

    return list(final_queue)

# Leer los valores de la lista desde el teclado
values = input("Ingrese los valores de la lista separados por espacios: ")
queue = deque(map(int, values.split()))

# Imprimir la lista ordenada
print("Lista ordenada:", sort_queue(queue))

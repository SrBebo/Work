from collections import deque
values= [8, 3, 2, 1]

def sort_queue(queue): #function to sort the queue
    if len(queue) <= 1: #if the length of queue is less than or equal to 1
        return queue #return the queue
    
    half = len(queue) // 2 #get the half of queue
    sublist1 = deque([queue[i] for i in range(half)]) #create a sublist1 with the half of queue
    sublist2 = deque([queue[i] for i in range(half, len(queue))]) #create a sublist2 with the half of queue

    queue1 = deque(sort_queue(sublist1)) #sort the sublist1
    queue2 = deque(sort_queue(sublist2)) #sort the sublist2

    final_queue = deque()  #create a final queue
    while queue1 and queue2:   #while queue1 and queue2
        if queue1[0] < queue2[0]:  #if the first element of queue1 is less than the first element of queue2
            final_queue.append(queue1.popleft()) #append the first element of queue1 to final queue
        else:
            final_queue.append(queue2.popleft()) #append the first element of queue2 to final queue
    final_queue.extend(queue1) #extend the final queue with queue1
    final_queue.extend(queue2) #extend the final queue with queue2

    return list(final_queue) #return the final queue

queue = deque(values) #create a queue with the values

print("Sorted list:", sort_queue(queue)) #print the sorted queue

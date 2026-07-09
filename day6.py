queue=[]
size=10
def enqueue(value):
    if len(queue)==size:
        print("Queue is full")
    else:
        queue.append(value)
def dequeue(value):
    if len(queue)==0:
        print("Queue is empty")
    else:
        queue.pop(0)
def insert_front(value):
    if len(queue)==size:
        print("Queue is full")
    else:
        queue.insert(0,value)
def insert_rear(value):
    if len(queue)==size:
        print("Queue is full")
    else:
        queue.insert(-1,value)
def mid_add(value):
    if len(queue)==size:
        print("Queue is full")
    else:
        n=len(queue)//2
        queue.insert(n,value)
enqueue(10)
enqueue(20)
enqueue(30)
print("Queue",queue)

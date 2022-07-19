import queue as q

fifo = q.Queue()
lifo = q.LifoQueue()
simple = q.SimpleQueue()
priority = q.PriorityQueue()

message = "This is a Message for queue {}"
for counter in range(1,5):
    fifo.put(message.format(counter))
    lifo.put(message.format(counter))
    simple.put(message.format(counter))
    priority.put(message.format(counter))

# Checking Size
print("FIFO Size:: ", fifo.qsize())
print("LIFO Size:: ", lifo.qsize())
print("SIMPLE Size:: ", simple.qsize())
print("PRIORITY Size:: ", priority.qsize())

# getting the message from queue
fifo_get = fifo.get()
print("FIFO :: ", fifo_get)
lifo_get = lifo.get()
print("LIFO :: ", lifo_get)
simple_get = simple.get()
print("SIMPLE :: ", simple_get)
priority_get = priority.get()
print("PRIORITY :: ", priority_get)

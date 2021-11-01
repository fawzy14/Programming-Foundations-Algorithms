from collections import deque

queue = deque()

queue.append(1) #add 
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
                  # in queue fist in fist out 
x = queue.popleft() #remove # popleft remove the fist item in queue 
print(x)
print(queue)
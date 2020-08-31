class RingBuffer:
    def __init__(self, capacity):
        self.capacity  = capacity
        self.storage = [None] * capacity
        self.size = 0
  
    def append(self, item):
        self.storage[self.size] = item
        self.size = (self.size + 1) % self.capacity

    def get(self):
        return [i for i in self.storage if i is not None]


buffer1 = RingBuffer(5)

for i in range(50):
    buffer1.append(i)

buffer2 = RingBuffer(5)

buffer2.append(1)
buffer2.append(2)
buffer2.append(3)
buffer2.append(4)
buffer2.append(5)
buffer2.append(6)
buffer2.append(7)

print(buffer1.get())
print(buffer2.get())


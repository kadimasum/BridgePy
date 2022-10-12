
class Queue:
    queue = [] 
    back, front = 0,0

    @classmethod
    def enqueue(cls, num):
        cls.queue.append(num)
        cls.back += 1

    @classmethod
    def dequeue(cls):
        if len(cls.queue) == 0: return -1

        dequeued = cls.queue.pop(cls.front)
        cls.back -= 1

        return dequeued

queue1 = Queue()
queue1.enqueue(3)
queue1.enqueue(4)
queue1.dequeue()
queue1.enqueue(8)
queue1.enqueue(74)
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()


print(queue1.dequeue())
print(queue1.queue)
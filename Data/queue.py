class Queue:
    """
    FIFO SinglyLinkedList -> First In First Out LinkedList, first comes, first served:
        - Enqueue:
            Add a value to the end of the queue, this values becomes the tail
        - Deque:
            Removes the current leading value of the queue, in a singly linked list it is the head.
            After removing, points to a new head value
        - Peek:
            Check the current head value;
    """
    def __init__(self):
        self.queue = list()

    def enqueue(self, v):
        self.queue.append(v)

    def deque(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

    def displayQueue(self):
        return self.queue

    def displaySize(self): return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.displayQueue()
    q.deque()

"""
Stack Data Structure implementation.
    A stack follows the logic bellow:
        A <- B <- C <- D 
    This being our data
    To add a value to our data, it would come after the D. 
        A <- B <- C <- D <- E
    Now, the head of the values is E, and the previous value is D

    It is important to note that in a Stack, the values are being added to the end of the stack, which means that A is the oldest value, inacessible in our strucuture, and E is the newest one.

    The methods of a Stack are:
        Push: to add a new head value;
        Pop: to remove the current head value;
        Peek: to show the current head value;
"""
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar
T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    prev: Optional['Node[T]'] = None
    
class Stack(Generic[T]):
    def __init__(self):
        self.length:int = 0
        self.head: Optional[Node[T]] = None
    
    def push(self, item: T) -> None:
        node = Node(item, self.head)
        self.head = node
        self.length += 1

    def pop(self) -> Optional[T]:
        if not self.head:
            return None
        
        curr_len = self.length
        self.length = 0 if curr_len == 1 else curr_len -1
        popped_val = self.head.value
        self.head = self.head.prev

        return popped_val

    def peek(self) -> Optional[T]:
        return self.head.value if self.head else None


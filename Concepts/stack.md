# Stacks!
- Queues, but backwards
- Instead of A -> B -> C -> D; A <- B <- C <- D
- to add, it would be:
    ... C <- D <- *E ..., where E is the new value
    - the previous head, D, now points to E.

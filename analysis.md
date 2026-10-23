# Analysis: Stacks and Queues Implementation Decisions

1. _Why the linked-list stack pushes at the head instead of the tail:_
   A linked-list stack performs insertions and removals at the head because both operations can be executed in constant time $O(1)$. If operations were performed at the tail of a singly linked list, removing an element (popping) would require traversing the entire list to locate the second-to-last node, resulting in an inefficient $O(n)$ time complexity.

2. _Why the array queue must be circular:_
   A naive linear array queue causes front indices to continuously move forward upon every dequeue, leaving unused wasted space at the beginning of the array or requiring costly $O(n)$ element shifts. Utilizing a circular array structure with modulo arithmetic allows empty slots at the front of the array to be reused seamlessly when the rear wraps around, optimizing memory and maintaining $O(1)$ efficiency for both enqueues and dequeues.

##Arrays

An array is a contiguous collection of the same data type. It is a linear collection, thus objects are stored one after the other in memory. In an array you can read the element at a specific index.

|Access|Search|Insertion|Deletion|
|:-:|:-:|:-:|:-:|:-:|
|O(1)|O(n)|O(n)|O(n)|

Access - via index
Search - must look at each individual element in array until item is found
Insertion - insertion at an index requires moving all other items to the left by one
Deletion - deletion at an index requires moving all other items to the right by one

Advantages
- Allows for random access via indeces
- 

Disadvantages
- Size of array must be defined on creation and cannot dynamically add more space to the array
- All elements must be of the same data type

##Linked Lists

A linked list is a collection of nodes, each of which stores some data.

###Singly Linked

In a singly linked list, each node contains some data and a pointer to the next node.

|Access|Search|Insertion|Deletion|
|:-:|:-:|:-:|:-:|:-:|
|O(n)|O(n)|O(1)|O(1)|

###Doubly Linked

In a doubly linked list, each node contains some data, a pointer to the next node and a pointer to the previous.

|Access|Search|Insertion|Deletion|
|:-:|:-:|:-:|:-:|:-:|
|O(n)|O(n)|O(1)|O(1)|

###Circular Linked


##Arrays vs. Linked lists

Queues

Stacks

Hash Maps

- Handling Collisions

Heaps

Trees

- Binary Trees
- Binary Search Trees
- Tries
- Self Balancing Trees

Graphs

- Edge list
- Adjacency list
- Adjacency matrix
##Linear Data Structures

The following data structures are defined as linear. This is because they are collections of data that are stored sequentially. These structures have defined start and end values. Each element has a next/previous element.

##Arrays

An array is a contiguous collection of the same data type. It is a linear collection, thus objects are stored one after the other in memory. In an array you can read the element at a specific index.

|Average||||Worst||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|O(1)|O(n)|O(n)|O(n)|O(1)|O(n)|O(n)|O(n)|

Access - via index
Search - must look at each individual element in array until item is found
Insertion - insertion at an index requires moving all other items to the left by one
Deletion - deletion at an index requires moving all other items to the right by one

##Linked Lists

A linked list is a collection of nodes, each of which stores some data and has one or two pointers. Pointers that do not point to anything are null pointers.

|Average||||Worst||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|O(n)|O(n)|O(1)|O(1)|O(n)|O(n)|O(1)|O(1)|

###Singly Linked

In a singly linked list, each node contains some data and a pointer to the next node.

###Doubly Linked

In a doubly linked list, each node contains some data, a pointer to the next node and a pointer to the previous.

####Application
In Operating Systems doubly linked lists are used to reference active processes, threads, and other dynamic objects. Some rootkits avoid detection by unlinking themselves from these lists.

###Circular Linked

In a circular linked list, each node contains some data and a pointer to the next node. The last node contains a pointer to the first node.

##Arrays vs. Linked lists

|Array|Linked list|
|-|-|
|Fixed size, defined on creation|Variable size, new nodes added when needed|
|Can contain unused memory bits|Only memory which is needed is used|
|Only requires one piece of memory per element|Requires one piece of memory and at least one extra bit for storing a pointer|
|Can access any element at a specific index|Must traverse to find element|
|Memory may not be available as one large block|Memory may be available as multiple small blocks|

##Stacks

A stack is a linear data structure wherein the last element added to it is the first to be removed from it, commonly known as last in, first out'.

When elements are pushed on to the stack. they are added to the 'top' of the queue. When items are removed from the stack, they are removed from the top of the stack.

####Applications

1. Function calls: most compilers implement function calls by using a stack.
2. Eliminating recursion from a program: instead of calling a function recursively, the programmer uses a stack to simulate the function calls in the same way that the compiler would have done so.
3. Deapth First Search.

##Queues

A queue is a linear structure wherein the first element added to it is the first element that will be removed from it, commonly known as 'first in, first out'. 

When elements are pushed into the queue they are placed directly at the end. When elements are removed from the queue they are removed from the front.

####Applications

1. When serving requests of a single shared resource e.g. print job scheduling and process scheduling in an OS. 
2. Transferring data asynchronously between two processes (IO buffers), e.g., pipes, file IO, sockets.
3. Interrupt handling: When programming a real-time system that can be interrupted (e.g., by a mouse click or wireless connection), it is necessary to attend to the interrupts immediately, before proceeding with the current activity.
3. Breadth First Search.



##Hash Maps / Hash tables

A hash map is implemented by using both a **hash function** and a **hash table**. A hash function takes a **key value** as input and outputs a **hash value**. The hash value maps the key to a specific index in the hash table.

Initially, you would use the hash function to determine where in a hash table a given key would be stored. Later you would use the same hash function to search for a given key.

Hash functions must behave consistenly and output the same value for any given key. 

Good hash functions:
* make use of all information provided by a key
* uniformly distributes output across table
* maps similar keys to very different hash values

|Average|||Worst|||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Search|Insertion|Deletion|Search|Insertion|Deletion|
|O(1)|O(1)|O(1)|O(n)|O(n)|O(n)|

###Handling Collisions

A collision occurs when two keys hash to the same hash value. As a result two keys must be stored at the same value. This can be handled in different ways.

###Open addressing

If a key hashes to the same index as a previously stored key, it is assigned 
to another available slot in the table.

Three ways of open addressing:
1. Linear probing: At collision, the new key is assigned to the next available slot in the table.
2. Quadratic Probing: At collision, the new key is assigned to the i<sup>2</sup>th slot.
3. Double Hashing: At collision, we use another hash function doublehash() and look for the i*doublehash(x)<sup>th</sup> slot in the table.

Comparison:
1. Linear probing has the best cache performance, but suffers from clustering. One more advantage of Linear probing is easy to compute.
2. Quadratic probing lies between the two in terms of cache performance and clustering.
3. Double hashing has poor cache performance but no clustering. Double hashing requires more computation time as two hash functions need to be computed.

###Seperate chaining

In seperate chaining each hash value maps to an index on a hashtable. However, the key value is stored in a linked list which the hash index points to.

If a key hashes to the same index as a previously stored key, it is inserted into the front of the linked list.

It is mostly used when it is unknown how many and how frequently keys may be inserted or deleted.

###Linear probing vs. Seperate chaining

|Linear probing|Seperate Chaining|
|:-:|:-:|
|Worst case insertion time is O(n)|Worst case insertion time is O(1)|
|Worst case search time is O(n)|Worst case search time is O(n/k) (although k is a constant, it still makes a slight difference)|
|Hash table has finite space|Hash table never fills up as new values are stored in linked lists|
|Provides better cache performance as everything is stored in same table|Cache performance is not good as keys are stored using linked list|
|Stores everything in the hash table with assigned memory|Uses extra space for links|
|Very sensitive to the hash function|Not sensitive to the hash function|


###Applications

1. Hash tables are used when fast insertion, deletion and lookup are a priority e.g. a contact list.
2. In security passwords are hashed and stored so that only the user knows the password, maintaining privacy. 


##Trees

There are many different types of tree data structures, however all of them follow the basic rules outlined below.

A tree is a non-linear data structure that is a collection of nodes linked together to simulate hierarchy. The topmost node in a tree is called the **root** node, there is only ever one root node. Each node contains some data, and this data can be of any type.

Aside from the root node, all other nodes have one **parent** node. All nodes can have **child** nodes. Children of the same node can all be referred to as **siblings**. A node without children is called a **leaf** node. All nodes that have children can be referred to as **internal** nodes. An **edge** is a link between a node and its parent. 

In a tree there are n nodes. By definition, there are exactly n - 1 edges in a tree, because all nodes except the root node have an incoming edge.

The **depth** of a node x is the number of edges in the path from the root node to the node x. All nodes with the same depth are at the same **level**.The **height** of a tree is the longest path from the root node to a leaf.

The height of an empty tree is _-1_ and the height of a tree with one node (just the root node) is _0_.

A tree can have many subtrees. Recursion is reducing something in a self similar manner. Trees have this recursive property and it is used in many of its implimentations.

###Applications
1. Storing naturally hierarchical data e.g. a file system
2. Organising data for quick search, insertion and deletion e.g. Binary Search Trees

##Binary Trees

Binary trees (BTs) are a tree type where each node can have a maximum of two child nodes. In the case of two child nodes they can be called the left child and the right child.

Binary Trees can be implemented by defining each node structure with two pointers and one data property. The pointers are used to store the locations of both child nodes of the current node and the data property holds the node's value.

Maximum number of _nodes at a level i_ = 2<sup>_i_</sup>.

Maximum number of _nodes in a binary tree with height h_ = 2<sup>_h+1_</sup> - 1.

###Classifications of binary trees

1. Strict/Proper binary tree - in this BT each node can have either 0 or 2 children.
2. Complete binary tree - all levels, with or without the last level, are completely filled and all nodes are as left as possible.
3. Perfect binary tree -  all levels are filled. _total nodes_ = 2<sup>_h+1_</sup> - 1.
4. Balanced binary tree - difference between height of left and right subtree for every node is not more than _k_ (mostly 1).

##Binary Search Trees

In a Binary Search Tree (BST), for each node, the value of all the nodes in the left subtree are lesser and the values of all nodes in the right subtree are greater.

A balanced BST is one where all nodes to the right of the root are greater and all those to the left of the root node are smaller. The difference between the height of left and right subtrees for every node is not more than 1. Balanced BSTs have a recursive structure; as you traverse further into the structure the size of the search space halves.

|Average||||Worst||||
|Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|O(log(n))|O(log(n))|O(log(n))|O(log(n))|O(1)|O(n)|O(n)|O(n)|

##Binary Heaps

A binary heap is a type of complete binary tree. It can be either a min heap or a max heap. In a binary heap, the root node of any tree or subtree must be the smallest value (for a min heap) or the highest value (for a max heap).

Many operations can be performed on a binary heap:
* getMin() or getMax() - It returns the root element of the Heap. Time Complexity of this operation is O(1).
* extractMin() or extractMax() - Removes the min/max element from the heap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
* insert(): Inserting a new key takes O(Logn) time. We add a new key at the end of the tree. If the new key is greater/smaller (for min/max respectively) than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
* delete(): Deleting a key also takes O(Logn) time. We replace the key to be deleted with minum infinite by calling decreaseKey(). After decreaseKey(), the minus infinite value must reach root, so we call extractMin() to remove key. 

####Applications
1. Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time. Binomoial Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also efficiently.
2. Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.
3. Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra’s Shortest Path and Prim’s Minimum Spanning Tree.

##Tries

##Graphs

- Edge list
- Adjacency list
- Adjacency matrix

###References:
* Linked lists: https://en.wikipedia.org/wiki/Linked_list
* Running times: http://bigocheatsheet.com/
* Stacks and Queues: http://introcs.cs.princeton.edu/java/43stack/
* Hash tables: https://www.youtube.com/watch?v=h2d9b_nEzoA
* Seperate chaining: http://courses.csail.mit.edu/6.006/fall09/lecture_notes/lecture05.pdf
* Open addressing 1: http://courses.csail.mit.edu/6.006/fall11/lectures/lecture10.pdf
* Open addressing 2: https://www.cse.cuhk.edu.hk/irwin.king/_media/teaching/csc2100b/tu6.pdf
* Trees: https://www.youtube.com/watch?v=qH6yxkw0u78&index=25&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P
* Binary Heaps: http://geeksquiz.com/binary-heap/


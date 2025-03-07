# ieee cs cc

## **Overview**

This repository contains implementations of fundamental data structures and algorithms in Python. The tasks are organized into three levels of complexity, from basic to advanced composite data structures. Each level demonstrates various techniques and best practices, ensuring efficiency and optimal performance.

---

## **Table of Contents**

1. [Level 0: Doubly Linked List](#level-0-doubly-linked-list)
2. [Level 1: Stack with Min/Max Support](#level-1-stack-with-minmax-support)
3. [Level 2: Interval Merger](#level-2-interval-merger)
4. [Level 3: Cache with Expiry](#level-3-cache-with-expiry)
5. [Technologies Used](#technologies-used)
6. [Setup Instructions](#setup-instructions)
7. [Contributing](#contributing)

---

## **Level 0: Doubly Linked List**

### **Features Implemented**
- **Node Creation**: Each node contains `data`, `prev`, and `next` pointers.
- **Insertion**: Insertions at both the head and tail of the list.
- **Traversal**: Forward and backward traversals, printing each node’s data.

### **Technologies Used**
- **Python**: Python 3.x for implementation.
- **Data Structures**: Doubly Linked List.

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure Python 3.x is installed.
3. Run the script directly.

```bash
python doubly_linked_list.py
```

### **Implementation Details**
- **Node Class**: Defines a node with `data`, `prev`, and `next` pointers.
- **Insertion at Head and Tail**: Each method inserts a new node at the beginning or end of the list, adjusting pointers accordingly.
- **Traversal**: Forward and backward traversals are implemented for printing the entire list.

---

## **Level 1: Stack with Min/Max Support**

### **Features Implemented**
- **push(x)**: Pushes element onto the stack.
- **pop()**: Removes the top element from the stack.
- **top()**: Returns the top element without removing it.
- **getMin()**: Returns the minimum element in the stack.
- **getMax()**: Returns the maximum element in the stack.

### **Technologies Used**
- **Python**: Python 3.x for implementation.
- **Data Structures**: Stack, Min Stack, Max Stack.

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure Python 3.x is installed.
3. Run the script directly.

```bash
python stack_with_min_max.py
```

### **Implementation Details**
- **Main Stack**: Stores the elements.
- **Min Stack**: Tracks the minimum element.
- **Max Stack**: Tracks the maximum element.
- **Operations**: All operations (`push`, `pop`, `top`, `getMin`, `getMax`) are optimized for O(1) time complexity.

---

## **Level 2: Interval Merger**

### **Features Implemented**
- **addInterval(start, end)**: Adds a new interval, merging it with existing intervals if overlapping.
- **getIntervals()**: Returns the list of non-overlapping intervals, sorted by their starting time.

### **Technologies Used**
- **Python**: Python 3.x for implementation.
- **Data Structures**: List, Bisect, Sorting.

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure Python 3.x is installed.
3. Run the script directly.

```bash
python interval_merger.py
```

### **Implementation Details**
- **Insertion**: Uses `bisect.insort` for sorted insertion of intervals.
- **Merging**: After each insertion, intervals are merged to ensure no overlaps remain.
- **Sorting**: Intervals are always kept sorted for efficient merging.

---

## **Level 3: Cache with Expiry**

### **Features Implemented**
- **set(key, value, expiryTime)**: Stores the key-value pair with an expiration timestamp.
- **get(key)**: Retrieves the value if the key exists and hasn’t expired.
- **Automatic Expiry**: Automatically removes expired keys upon accessing `set()` or `get()`.

### **Technologies Used**
- **Python**: Python 3.x for implementation.
- **Data Structures**: Dictionary, Min-Heap.

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure Python 3.x is installed.
3. Run the script directly.

```bash
python expiry_cache.py
```

### **Implementation Details**
- **Min-Heap**: A heap is used to track expiry timestamps efficiently.
- **set()**: Adds key-value pairs with expiry times, pushes them into the heap.
- **get()**: Checks the heap and removes expired keys before fetching the value.
- **Automatic Expiry**: Expired keys are cleaned up automatically during each operation.

---

## **Technologies Used**

- **Python 3.x**: All code is written in Python 3.x.
- **Data Structures**:
  - Level 0: **Doubly Linked List**
  - Level 1: **Stack with Min/Max Support**
  - Level 2: **Interval Merger**
  - Level 3: **Cache with Expiry (Min-Heap)**

---

## **Setup Instructions**

To run any of the tasks, follow these instructions:

1. **Clone** or **download** the repository to your local machine.
2. Ensure **Python 3.x** is installed. If not, download it from [python.org](https://www.python.org/downloads/).
3. Open a terminal and run the relevant script for the task:

```bash
# To run Level 0 (Doubly Linked List)
python doubly_linked_list.py

# To run Level 1 (Stack with Min/Max Support)
python stack_with_min_max.py

# To run Level 2 (Interval Merger)
python interval_merger.py

# To run Level 3 (Cache with Expiry)
python expiry_cache.py
```

---




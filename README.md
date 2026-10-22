# Avaloka AI Intern Assignment
## Data Structures & Systems Design

**Submitted by:** Gowthami Kanchi  
**Language:** Python 3

## Overview

This repository contains solutions for the Avaloka AI Intern assignment. It covers data structures, algorithm design, time and space complexity, and system design concepts.

## Problem 1: LRU Cache Implementation

Implemented a Least Recently Used (LRU) Cache using a **hash map and a doubly linked list**.

### Features
- `get(key)`: Returns the value for an existing key or `-1` if the key is not found.
- `put(key, value)`: Inserts or updates a key-value pair.
- Automatically evicts the least recently used entry when the cache reaches capacity.
- Handles zero capacity and updates to existing keys.

**Time complexity:** Average O(1) for both `get()` and `put()`.

## Problem 2: Event Scheduler

Implemented two functions to manage meeting schedules.

### Functions
- `can_attend_all(events)`: Returns `True` if all events can be attended without overlapping, otherwise returns `False`.
- `min_rooms_required(events)`: Calculates the minimum number of meeting rooms required.

### Approach
- Sort events by start time.
- Detect overlaps by comparing consecutive events.
- Use a min-heap to track meeting end times and reuse rooms when meetings finish.
- Treat adjacent events as non-overlapping.

**Time complexity:** O(n log n) for both functions, where n is the number of events.

## Complexity Analysis

| Function | Time Complexity | Space Complexity |
|---|---|---|
| `LRUCache.get()` | Average O(1) | O(1) auxiliary |
| `LRUCache.put()` | Average O(1) | O(1) auxiliary |
| `can_attend_all()` | O(n log n) | O(n) |
| `min_rooms_required()` | O(n log n) | O(n) |

The LRU cache uses O(c) total storage, where c is its capacity.

## Example

```python
events = [(9, 10), (10, 11), (11, 12)]

print(can_attend_all(events))      # True
print(min_rooms_required(events))  # 1
```

## System Design Discussion

The assignment also discusses:
- Trade-offs of using a hash map with a doubly linked list.
- Extending the scheduler to assign specific room numbers.
- Making the LRU cache thread-safe using locks.

## How to Run

1. Install Python 3.
2. Clone this repository.
3. Run the Python file containing the implementations.

```bash
python lru.py
```

## Author

Gowthami Kanchi  

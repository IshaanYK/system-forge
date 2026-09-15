"""
High-throughput circular ring buffer data structure.
"""

from typing import Generic, Optional, TypeVar, List

T = TypeVar('T')

class RingBuffer(Generic[T]):
    """Fixed-capacity circular buffer with O(1) enqueue and dequeue operations."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._buffer: List[Optional[T]] = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def push(self, item: T) -> None:
        """Appends item to ring buffer, overwriting oldest entry if full."""
        self._buffer[self._tail] = item
        self._tail = (self._tail + 1) % self.capacity
        if self._size < self.capacity:
            self._size += 1
        else:
            self._head = (self._head + 1) % self.capacity

    def pop(self) -> Optional[T]:
        """Dequeues the oldest item in the buffer, or None if empty."""
        if self._size == 0:
            return None
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self.capacity
        self._size -= 1
        return item

    def is_full(self) -> bool:
        return self._size == self.capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

"""
High-performance LRU (Least Recently Used) cache implementation with O(1) ops.
"""

from typing import Dict, Optional, Any

class _Node:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self.prev: Optional['_Node'] = None
        self.next: Optional['_Node'] = None

class LRUCache:
    """Thread-safe capable LRU Cache utilizing a doubly linked list and hash map."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[str, _Node] = {}
        self.head = _Node("", None)
        self.tail = _Node("", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: _Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None

    def put(self, key: str, value: Any) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = _Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

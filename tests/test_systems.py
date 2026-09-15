"""
Unit tests for ring buffer and LRU cache implementations.
"""

import unittest
from system_forge.ring_buffer import RingBuffer
from system_forge.lru_cache import LRUCache

class TestSystemForge(unittest.TestCase):
    def test_ring_buffer(self):
        rb = RingBuffer(3)
        rb.push(1)
        rb.push(2)
        rb.push(3)
        self.assertTrue(rb.is_full())
        rb.push(4) # Overwrites 1
        self.assertEqual(rb.pop(), 2)
        self.assertEqual(rb.pop(), 3)
        self.assertEqual(rb.pop(), 4)
        self.assertTrue(rb.is_empty())

    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        self.assertEqual(cache.get("k1"), "v1")
        cache.put("k3", "v3") # Evicts k2
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k3"), "v3")

if __name__ == '__main__':
    unittest.main()

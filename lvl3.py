import heapq
import time

class TimeBasedCache:
    def __init__(self):
        self.cache = {}
        self.expiry_heap = []

    def set(self, key: str, value: str, expiryTime: int):
        # Store key-value and expiry timestamp in the cache
        timestamp = int(time.time())
        expiry_timestamp = timestamp + expiryTime
        self.cache[key] = (value, expiry_timestamp)
        
        # Insert the expiry timestamp into the heap
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))

    def get(self, key: str):
        # Clean expired entries before getting the value
        self._clean_expired_entries()
        
        if key in self.cache:
            return self.cache[key][0]  # Return value if not expired
        return None

    def _clean_expired_entries(self):
        current_time = int(time.time())
        
        # Remove expired keys from cache and heap
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            _, expired_key = heapq.heappop(self.expiry_heap)
            if expired_key in self.cache:
                del self.cache[expired_key]

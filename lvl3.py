import heapq
import time

class ExpiryCache:
    def __init__(self):
        self.cache = {}  # Stores key-value pairs
        self.expiry_heap = []  # Min-heap to track expiry timestamps

    def set(self, key, value, expiryTime):
        expiry_timestamp = time.time() + expiryTime  # Calculate expiry timestamp
        self.cache[key] = (value, expiry_timestamp)  # Store value and its expiry time
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))  # Push to heap

    def get(self, key):
        self._clean_expired()
        return self.cache.get(key, (None, None))[0]  # Return the value if it exists and hasn't expired

    def _clean_expired(self):
        current_time = time.time()
        # Clean expired keys from the heap
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            _, expired_key = heapq.heappop(self.expiry_heap)
            if expired_key in self.cache and self.cache[expired_key][1] <= current_time:
                del self.cache[expired_key]

# Usage Example
cache = ExpiryCache()
cache.set("user1", "John", 5)  # expires in 5 seconds
time.sleep(6)  # Simulate expiry time
print(cache.get("user1"))  # Expected Output: None


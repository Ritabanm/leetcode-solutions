class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        
        char_to_count = defaultdict(int)
        for ch in s:
            char_to_count[ch] += 1
        
        max_heap = []
        for key, val in char_to_count.items():
            max_heap.append((-val, key))
        heapify(max_heap)

        result = []
        window = set()
        
        while max_heap:
            if len(result) >= k:
                char_to_remove = result[len(result) - k]
                window.discard(char_to_remove)
            
            temp_storage = []
            found = False
            
            while max_heap and not found:
                val, key = heappop(max_heap)
                
                if key not in window:
                    result.append(key)
                    window.add(key)
                    if val < -1:
                        heappush(max_heap, (val + 1, key))
                    found = True
                else:
                    temp_storage.append((val, key))
            
            for item in temp_storage:
                heappush(max_heap, item)
            
            if not found:
                return ""
        
        return "".join(result)
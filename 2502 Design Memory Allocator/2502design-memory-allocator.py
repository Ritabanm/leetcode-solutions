class Range:
    def __init__(self, start, end):
        self.start = start 
        self.end = end
    
    def size(self):
        return self.end - self.start
    
    def __repr__(self):
        return "{start}..{end}".format(start=self.start, end=self.end)

class Allocator:

    def __init__(self, n: int):
        # capacity keeps track of overall memory available. It can straightway reject
        # allocation requests without iterating over the available memory.
        # This field gets updated during allocation and free.
        self.capacity = n
        # maintains a list of available memory ranges. During initialization its (0, n)
        # When allocate is  called, we iterate over the available ranges and if the width
        # of the range is big enough to accomodate the allocation size, we allocate and shrink
        # that range itself
        # During free, we sort the available ranges and try to defragment the memory by merging 
        # those ranges. Since the list is already sorted, merging is little straightforward.
        self.available = [Range(0, n)]
        # keeps track of memory used by processes. {mID => Vec<Range>}
        self.used = {} # mID to list of ranges 
        
    def allocate(self, size: int, mID: int) -> int:
        if size > self.capacity:
            return -1
        for avail_units in self.available:
            if size <= avail_units.size():
                self.capacity -= size
                start_use = avail_units.start
                avail_units.start += size
                if mID not in self.used:
                    self.used[mID] = [Range(start_use, start_use+size)]
                else:
                    self.used[mID].append(Range(start_use, start_use+size))
                return start_use
        return -1
        
    def defrag(self):
        merged_ranges = []
        idx = 0
        while idx < len(self.available):
            can_merge = True
            i = idx + 1
            while can_merge and i < len(self.available):
                if self.available[idx].end == self.available[i].start:
                    self.available[idx].end = self.available[i].end
                    i += 1
                else:
                    can_merge = False
            merged_ranges.append(self.available[idx])
            idx = i
        self.available = merged_ranges

    def freeMemory(self, mID: int) -> int:
        total_freed = 0
        old_used = self.used
        if mID not in self.used:
            return 0
        for used_space in self.used[mID]:
            total_freed += used_space.size()
            self.available.append(used_space)
        del self.used[mID]
        self.available = sorted(self.available, key=lambda x: x.start)
        self.defrag()
        self.capacity += total_freed
        return total_freed
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
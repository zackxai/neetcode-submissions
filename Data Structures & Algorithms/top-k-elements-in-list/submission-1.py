import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Frequency count nikaalo
        count = Counter(nums)
        
        # Step 2: Min-Heap banao
        heap = []
        
        for num, freq in count.items():
            # (freq, num) daal rahe hain taaki frequency par sorting ho
            heapq.heappush(heap, (freq, num))
            
            # Agar k se zyada elements hue, toh sabse choti frequency wala pop
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Result return karo (sirf numbers nikaal kar)
        return [pair[1] for pair in heap]
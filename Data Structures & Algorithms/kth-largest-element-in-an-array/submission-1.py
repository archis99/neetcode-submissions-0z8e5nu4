class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minh = []
        heapq.heapify(minh)
        for num in nums:
            heapq.heappush(minh, num)
            
            if len(minh) > k:
                heapq.heappop(minh)
        
        return minh[0]
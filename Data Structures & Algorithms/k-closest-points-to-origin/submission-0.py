class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minh = []
        for x, y in points:
            dist = (x * x) + (y * y)
            minh.append((dist, x, y))
        
        heapq.heapify(minh)

        while k > 0:
            dist, x, y = heapq.heappop(minh)
            res.append([x, y])
            k-=1

        return res
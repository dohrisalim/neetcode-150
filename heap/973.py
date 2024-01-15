class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            diff = (x ** 2) + (y ** 2)
            minHeap.append([diff,x,y])
        
        heapq.heapify(minHeap)
        ans = []
        while k > 0:
            diff, x, y = heapq.heappop(minHeap)
            ans.append([x,y])
            k -= 1
        return ans
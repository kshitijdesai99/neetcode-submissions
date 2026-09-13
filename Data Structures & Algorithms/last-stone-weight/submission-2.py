class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)!=1:
            print(stones)
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if(a==b):
                heapq.heappush(stones,0)
            else:
                if a<b:
                    heapq.heappush(stones,a-b)
                else:
                    heapq.heappush(stones,b-a)
        # Time complexity - O(nlogn)
        # Space complexity - O(1)
        return -stones[0]

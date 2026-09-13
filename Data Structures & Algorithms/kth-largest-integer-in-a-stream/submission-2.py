class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    # Time complexity - O(klogk)
    # Space complexity - O(k)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    # Time complexity - O(log(k))
    # Space complexity - O(1)

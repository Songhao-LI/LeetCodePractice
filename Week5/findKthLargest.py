class Solution:
    def findKthLargest_select(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        def partition(nums, left, right):
            pivot = nums[left]
            # put small numbers on the left side
            # large numbers on the right side
            i = left + 1
            j = right
            while i <= j:
                if nums[i] > pivot:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
            nums[left], nums[j] = nums[j], nums[left]
            return j

        while left < right:
            pivot = self.partition(nums, left, right)
            if pivot == k - 1:
                return nums[k - 1]
            elif pivot > k - 1:
                right = pivot - 1
            else:
                left = pivot + 1
        return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we should sort the array in descending order
        # return res[k - 1]
        def quickSort(nums, left, right):
            # Base case： 当数组不可再分
            if left >= right:
                return
            pivot = partition(nums, left, right)
            quickSort(nums, left, pivot - 1)
            quickSort(nums, pivot + 1, right)
        def partition(nums, left, right):
            pivot = nums[left]
            # put small numbers on the left side
            # large numbers on the right side
            i = left + 1
            j = right
            while i <= j:
                if nums[i] > pivot:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
            nums[left], nums[j] = nums[j], nums[left]
            return j

        quickSort(nums, 0, len(nums) - 1)
        return nums[k-1]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # O(NlogN)
        # O(N)
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        res = -1
        for i in range(k):
            res = -heapq.heappop(max_heap)
        return res



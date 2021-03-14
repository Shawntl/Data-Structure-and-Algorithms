import sys
import time
import numpy as np

sys.setrecursionlimit(100000)

LEFT = lambda i: 2 * i + 1
RIGHT = lambda i: 2 * i + 2


class Sort:
    def time_count(fn):
        def wrapper(*args, **kw):
            start = time.time()
            fn(*args, **kw)
            end = time.time()
            cost = end - start
            print('%s executed in %s ms' % (fn.__name__, cost*1000))
            return fn(*args, **kw)

        return wrapper

    @time_count
    def Brute_Force(self, nums):
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

    @time_count
    def Select_Sort(self, nums):
        for i in range(len(nums)):
            mini = i
            j = i+1
            while j < len(nums):
                if nums[j] < nums[mini]:
                    mini = j
                j += 1
            if mini != i:
                nums[mini], nums[i] = nums[i], nums[mini]
        return nums

    @time_count
    def Bubble_Sort(self, nums):
        for i in range(len(nums)):
            j = len(nums) - 1
            while j > i:
                if nums[j] < nums[j-1]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        return nums

    @time_count
    def Insert_Sort(self, nums):
        for i in range(1, len(nums)-1):
            if nums[i] < nums[i-1]:
                mini = nums[i]
                j = i - 1
                while nums[j] > mini:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = mini
        return nums

    heap_size = 0
    @time_count
    def Heap_Sort(self, nums):
        self.BuildMaxHeap(nums)
        for i in range(len(nums)-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            Sort.heap_size -= 1
            self.KeepHeap(nums, 0)

    def BuildMaxHeap(self, nums):
        Sort.heap_size = len(nums)
        for i in range(len(nums)//2-1, -1, -1):
            self.KeepHeap(nums, i)

    def KeepHeap(self, nums, i):
        l, r = LEFT(i), RIGHT(i)
        largest = l if l < Sort.heap_size and nums[l] > nums[i] else i
        largest = r if r < Sort.heap_size and nums[r] > nums[largest] else largest

        if i != largest:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.KeepHeap(nums, largest)

        return

    @time_count
    def Merge_Time(self, nums):
        self.Merge_Sort(nums)

    def Merge_Sort(self, nums):
        n = len(nums)
        mid = n // 2
        left = nums[0:mid]
        right = nums[mid:n]
        if n < 2:
            return
        
        self.Merge_Sort(left)
        self.Merge_Sort(right)
        self.Merge(left, right, nums)

    def Merge(self, left, right, nums):
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[i+j] = left[i]
                i += 1
            else:
                nums[i+j] = right[j]
                j += 1
        
        if i == len(left):
            nums[i+j:] = right[j:]
        else:
            nums[i+j:] = left[i:]

    @time_count
    def Quick_Time(self, nums):
        self.Quick_Sort(nums)

    def Quick_Sort(self, nums):
        left = 0
        right = len(nums) - 1
        self.quick_sort(nums, left, right)

    def quick_sort(self, nums, left, right):
        if left < right:
            p = self.partition(nums, left, right)
            self.quick_sort(nums, left, p-1)
            self.quick_sort(nums, p+1, right)

    def partition(self, nums, left, right):
        b = right
        right = b - 1
        pivot = nums[b]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                left, right = left + 1, right - 1
        nums[b], nums[left] = nums[left], nums[b]
        return left

    @time_count
    def Count_Sort(self, nums):
        bucket = [0] * (max(nums) - min(nums) + 1)
        for num in nums:
            index = num - min(nums)
            bucket[index] += 1
        i = 0
        for j in range(len(bucket)):
            while bucket[j] > 0:
                nums[i] = j + min(nums)
                i += 1
                bucket[j] -= 1

    @time_count
    def Bucket_Sort(self, nums, bucket_size=100):
        minVal, maxVal = min(nums), max(nums)
        bucket_count = ((maxVal - minVal) // bucket_size) + 1
        buckets = []
        for i in range(bucket_count):
            buckets.append([])
        for num in nums:
            buckets[(num - minVal) // bucket_size].append(num)

        nums.clear()
        for bucket in buckets:
            self.Quick_Sort(bucket)
            nums.extend(bucket)

    @time_count
    def Radix_Sort(self, nums):
        bucket_count = 10
        div = 1
        loop_count = len(str(max(nums)))

        buckets = [[] for i in range(bucket_count)]

        while loop_count:
            
            for num in nums:
                buckets[num // div % bucket_count].append(num)

            i = 0
            for bucket in buckets:
                while bucket:
                    nums[i] = bucket.pop(0)
                    i += 1

            div *= 10
            loop_count -= 1


        


if __name__ == "__main__":
    nums = list(np.random.randint(low=-5000, high=5000, size=10000))
    Sort().Brute_Force(nums)
    Sort().Bubble_Sort(nums)
    Sort().Select_Sort(nums)
    Sort().Insert_Sort(nums)
    Sort().Heap_Sort(nums)
    Sort().Merge_Time(nums)
    Sort().Quick_Time(nums)
    Sort().Count_Sort(nums)
    Sort().Bucket_Sort(nums)
    Sort().Radix_Sort(nums)
    

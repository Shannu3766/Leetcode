
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.Quicksort(nums, 0, len(nums) - 1)

    def Partition(self, A, Lb, Ub):
        pivot = A[Lb]
        start = Lb + 1
        end = Ub

        while True:
            while start <= end and A[start] <= pivot:
                start += 1
            while start <= end and A[end] > pivot:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
            else:
                break

        A[Lb], A[end] = A[end], A[Lb]
        return end

    def Quicksort(self, A, Lb, Ub):
        if Lb < Ub:
            loc = self.Partition(A, Lb, Ub)
            self.Quicksort(A, Lb, loc - 1)
            self.Quicksort(A, loc + 1, Ub)

# Example usage
A = Solution()
nums = [2, 0, 2, 1, 1, 0]
A.sortColors(nums)
print(nums)

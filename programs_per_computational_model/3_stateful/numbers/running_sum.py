from typing import List

"""
    Analysis:
        N = number of elements in nums list
        Time = O(N)
        Space = O(N) + O(1) = O(N)
"""


def running_sum(nums: List[int]) -> List[int]:
    sums = [0] * len(nums)
    last_sum = 0
    for i in range(len(nums)):
        sums[i] = last_sum + nums[i]
        """
        This is the key to O(N) runtime, that is remembering the result of the computation.
        Making the next computation, the sum of the previous computation + the new value.
            This is consant time.
        """
        last_sum = sums[i]
    return sums

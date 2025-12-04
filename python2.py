from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])      # take x_i
            result.append(nums[i + n])  # take y_i
        return result

# Using Hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Using 2 pointer approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left][0] + nums[right][0]
            if current_sum == target:
                return [nums[left][1], nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

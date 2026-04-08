class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[nums[index]] = index
        for index, value in enumerate(nums):
            numberNeeded = target - nums[index]
            if numberNeeded in hashmap and hashmap[numberNeeded] != index:
                return [index, hashmap[numberNeeded]]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_Set = set()

        for num in nums:
            if num in map_Set:
                return True
            map_Set.add(num)
        return False

        
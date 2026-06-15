class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first, last, temp = 0, len(s)-1, float('inf')

        while first < last:
            temp = s[first]
            s[first] = s[last]
            s[last] = temp
            first +=1
            last -=1
            
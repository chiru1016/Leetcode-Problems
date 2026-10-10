class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        a = sorted(set(nums))
        l = len(a)
        if l>= 3:
            return a[-3]
        elif l<3:
            return a[-1]
        else:
            return nums
        
            

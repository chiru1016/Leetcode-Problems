class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        last = len(nums) - 1
        count = len(nums)
        while first<=last:
            if nums[first]!=val:
                first +=1
            elif nums[last]==val:
                last-=1
                count -=1
            else:
                nums[first], nums[last]= nums[last],nums[first]
                first+=1
                last-=1
                count -=1

        return count

            

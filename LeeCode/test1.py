# coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap= {}
        for index ,num in enumerate(nums):

            another_num = target - num
            print(another_num)
            print(hashmap)
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index
        return None

if __name__=='__main__':
    proj = Solution()
    result = proj.twoSum([8,7,11,15,5,4],13)
    print(result)
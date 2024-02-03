
class Solution(object):
    def twoSum(self, nums, target):
        list={}
        for i,num in enumerate(nums):
            x= target - num
            if x in list:
                return [list[x],i]
            list[num]= i
        return []         
 
nums=[56,78,5,7,8]
target=12       
obj1 =Solution()
result=obj1.twoSum(nums, target)
print(result)
#33333333333-or-
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

nums = [56, 78, 5, 7, 8]
target = 12
obj2 = Solution()
result2 = obj2.twoSum(nums, target)
print(result2)
#-------------test------------------
def twoSum( nums, target):
    list={}
    for i,num in enumerate(nums):
        x= target - num
        #print(num,i)
        #print(x)
        if x in list:
            print(list[x],i)
        list [num]=i
        print()
            
twoSum([5,6,7,8,8,56],9)    


def twoSum(nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               print(j)   
              
twoSum([5,6,7,8,8,3],16)             
##
class Solution1(object):
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            print(i)
twoSum([5,6,7,8,8,56],9)   
#-------------test------------------
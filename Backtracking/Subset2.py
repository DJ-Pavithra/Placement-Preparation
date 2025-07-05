# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subsetsWithDup(nums) :
    n=len(nums)
    nums.sort()
    res,sol=[],[]
    def backtrack(i):
        if i==n:
            res.append(sol[:])
            return
        
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop() 
        
        i+=1
        while i<n and nums[i]==nums[i-1]:
            i+=1
        backtrack(i)

    backtrack(0)
    return res
nums = [1,2,2]
result=subsetsWithDup(nums)
print(f"The output subsets:{result}")
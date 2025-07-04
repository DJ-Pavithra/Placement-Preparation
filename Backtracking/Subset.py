nums=[1,2,3]
def subsets(nums):
    n=len(nums)
    res,sol=[],[]
    
    def backtrack(i):
        if i==n:
            res.append(sol[:])
            return
        
        # Dont pick num[i]
        backtrack(i+1)
        # Pick num[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop() 
    backtrack(0)
    return res
sol=subsets(nums)
print(sol)

        
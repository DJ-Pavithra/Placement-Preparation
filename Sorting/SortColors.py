def sortColors(nums) :
        l,m=0,0
        h=len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l], nums[m] = nums[m], nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            elif nums[m]==2:
                nums[m], nums[h] = nums[h], nums[m]
                h-=1
            
nums= [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(f"Sorted colors: {nums}")

#or  using the built-in sort function
# nums.sort()
# print(f"Sorted colors: {nums}")
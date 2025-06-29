# Find indices of two numbers in an array that add up to a given target
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

in_arr=list(map(int,input("Enter the nums:").split()))
target=int(input("Enter the target value:"));

seen_num ={}

for i in range(len(in_arr)):
    diff= target-in_arr[i]
    
    if diff in seen_num:
        print(seen_num[diff],i)
        break
    else:
        seen_num[in_arr[i]]=i
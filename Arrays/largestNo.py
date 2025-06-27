arr = [5,3,92,62,8];

max_num =arr[0]
for num in arr:
    if num >max_num:
        max_num = num
        
# or

max_num2 = max(arr)
        
print(f"Largest num: {max_num}")
print(f"Largest num: {max_num2}")
arr= [1,2,3,4,5]

i,j=0, len(arr)-1
while i<j:
    arr[i], arr[j] = arr[j],arr[i]
    i+=1
    j-=1
        
# or
arr1=arr
arr1.reverse

print(f"Sorted array: {arr}")
print(f"Sorted array: {arr1}")
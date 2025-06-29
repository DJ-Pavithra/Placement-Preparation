def removeDuplicate(arr):
    unique_set=set()
    result_list=[]
    
    for i in arr:
        if i not in unique_set:
            unique_set.add(i)
            result_list.append(i)
    return result_list

arr=[1,2,3,4,5,2,1,4]
result=removeDuplicate(arr)
print(result)

# or

result2=set(arr)
print(list(result2))
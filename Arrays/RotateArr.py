def reverse(arr,i,j):
    while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    

def rotate(arr,k):
    n=len(arr)
    k=k % n
    # Reverse the entire array
    reverse(arr,0,n-1)
    
    # Reverse first k elements
    reverse(arr,0,k-1)
    
    # Reverse remaining n - k elements
    reverse(arr,k,n-1)
        
    print(arr)
       
arr=[1,2,3,4,5]
rotate(arr,2)
        
str1=input("Enter a string:")

i,j=0,len(str1)-1
flag=0
while i<j:
    if str1[i]!=str1[j]:
        flag=1
        break
    i+=1
    j-=1
if(flag):
    print("Not palindrome")
else:
    print("Palindrome")
    
# or

if str1 == str1[::-1]:
    print("Palindrome")
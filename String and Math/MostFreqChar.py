# Input: "banana"
# Output: "a"

str1=input("enter the string:").lower()

freq={}

result=0

ans=""

for ch in str1:
    freq[ch]=freq.get(ch,0)+1
    
for key,value in freq.items():
    if value>result:
       result=value
       ans=key
       
print(f"The most frequent character is: {ans}")

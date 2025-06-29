# Input: "listen", "silent"
# Output: True

str1=input("Enter the string:").lower()

str2=input("Enter the 2nd string:").lower()


if len(str1) != len(str2):
    print("Not anagram")

else:
    
    str1=sorted(str1)
    str2=sorted(str2)
    
    if str1 == str2:
        print("Anagram")
    else:
        print("Not anagram")

# or better optimized code without sorting:

if len(str1) != len(str2):
    print("Not anagram")
    
else:
    freq={}
    
    for ch in str1:
        freq[ch]=freq.get(ch,0)+1
        
    for ch in str2:
        freq[ch]=freq.get(ch,0)-1
    
    for value in freq.values():
        value+=value
    if value==0:
        print("Anagram")
    else:
        print("Not anagram")



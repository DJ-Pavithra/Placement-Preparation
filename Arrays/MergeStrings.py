# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

str1= input("enter first string")
str2= input("enter first string")
i,j=0,0
res=[]
while i<len(str1) and j<len(str2):
            res.append(str1[i])
            res.append(str2[j])
            i,j =i+1,j+1
res.append(str1[i:])
res.append(str2[j:])

print("".join(res))
        
    
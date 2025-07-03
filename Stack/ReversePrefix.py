# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# Example 1:

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

def reversePrefix( word: str, ch: str):
        stack=[]
        index=word.find(ch)
        if index ==-1:
            return word
        
        for i in range(index+1):
            stack.append(word[i])
        
        reverse_str=""
        while stack:
            reverse_str +=stack.pop()
  
        return reverse_str+word[index+1:]
    
word="abcdefd"
ch="d"
ans=reversePrefix(word,ch)
print(f"Reversed prefix: {ans}")
                
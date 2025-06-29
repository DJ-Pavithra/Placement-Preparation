#  Reverse Words in a String
#  Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#  Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

str1=input("Enter the words to reverse: ")
list1=str1.split()

l=len(list1)

list2= list1[l::-1]

print(" ".join(list2))

# or

print(" ".join(str1.split()[::-1]))
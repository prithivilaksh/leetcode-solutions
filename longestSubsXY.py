# Determine the maximum length of a subsequence from one string that is also a substring of another string. 
# A subsequence of a string is created by removing zero or more characters from it, while a substring consists of consecutive characters from the string.

# Given two strings x and y, determine the length of the longest subsequence of x that is also a substring of y.

# Example

# x='abcd'

# y='abdc'.

# The subsequences of "abcd" are "a", "b", "c", "d", "ab", "ac", "ad", "bc", "bd", "cd", "abc", "abd", "acd", "bcd", and "abcd".

# The substrings of "abdc" are "a", "b", "d", "c", "ab", "bd", "dc", "abd", "bdc",and "abdc".

# The longest subsequence of x that is also a substring of y is 'abd' with length 3.

# Function Description

# Complete the function longestSubsequence in the editor with the following parameter(s):

# string x: a string to find the subsequence of

# string y: a string to find the substring of

# Returns

# int the length of the longest subsequence of x that is a substring of y

# Constraints

# 1 lengths of x and y s 2000

# Strings x and y consist of lowercase English letters ascii(a-z).

from functools import cache

def longestSubsequence(x,y):

    m,n=len(x),len(y)
    
    @cache
    def dp(i,j):
        if i==m or j==n: return 0
        if x[i]==y[j]: return 1+dp(i+1,j+1)
        else: return dp(i+1,j)
    
    return max(dp(0,j) for j in range(n))



def longestSubsequence(x, y):

    max_length = 0
    m,n=len(x),len(y)

    for start in range(len(y)):
        i = length = 0 

        for end in range(start, len(y)):
            while i < len(x) and x[i] != y[end]:
                i += 1

            if i < len(x):
                i += 1
                length += 1
                max_length = max(max_length, length)
            else: break

    return max_length

if __name__=="__main__":
    print(longestSubsequence("abcd","abdc"))

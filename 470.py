# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            res=(rand7()-1)*7 + (rand7()-1) #[0-48]
            if res<=39: return res%10+1
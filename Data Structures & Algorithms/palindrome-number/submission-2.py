class Solution:
    def isPalindrome(self, x: int) -> bool:

        res = []
        if x < 0 or (x % 10 == 0 and x != 0): #edge case handling
            return False
        #convert int into a list
        while x > 0:
            res.append(x % 10) 
            x//= 10 #removes last digit
        res = res[::-1]
        
        
        l, r = 0, len(res)-1
        while l < r:
            if res[l] == res[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True
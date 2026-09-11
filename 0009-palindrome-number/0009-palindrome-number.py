class Solution(object):
    def isPalindrome(self,x):
        result=0
        orignal=x
        while x>0:
            ld=x%10
            result=(result*10)+ld
            x=x//10
              

       
        if result==orignal:
            return True
                
        return False            
            
class Solution:
    def findPosition(self, N , M , K):
        if N==1:
            return 1
        if (K+(M%N)-1)==N:
            return (K+(M%N)-1)
        else:
            return (K+(M%N)-1)%N

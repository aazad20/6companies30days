class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        i=1
        alice,bob = 0,0
        n = len(colors)
        while i<n:
            count=1
            while i<n and colors[i]==colors[i-1]:
                count+=1
                i+=1
                
            if count>2:
                if colors[i-1]=="A":
                    alice+=count-2
                else:
                    bob+=count-2
            print(alice,bob)
            i+=1
        if alice>bob:
            return True
        else:
            return False

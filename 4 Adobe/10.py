from collections import OrderedDict
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        dic = OrderedDict()
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        mk=""
        mv=-1
        for k,v in dic.items():
            if mv<v:
                mv=v
                mk=k
            elif mv==v:
                if k<mk:
                    mv=v
                    mk=k
                    
        return [mk,mv]

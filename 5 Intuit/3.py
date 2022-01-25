def missingNumber(string):
    def sto(s):
        x = 0
        for i in s:
            x=x*10 + (ord(i)-ord('0'))
        return x
    n = len(string)
    for k in range(1,7):
        temp =""
        l = k
        i = 0
        while i < n and l >0:
            temp+=string[i]
            i+=1
            l-=1
        prev=sto(temp)
        count=0
        j=i
        miss=0
        flag=0;
        temp=""    
        while j<n:
            temp+=string[j]
            j+=1
            if prev+1==sto(temp):
                prev=sto(temp)
                temp=""
            elif prev+2==sto(temp):
                count+=1
                miss = prev+1
                prev=sto(temp)
                temp=""
            elif prev <sto(temp):
                flag=1
        if flag==0 and count==1:
            return miss
    return -1

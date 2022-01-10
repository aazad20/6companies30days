def encode(arr):
    ans=""
    i=0
    while i <len(arr):
        count =1
        while(i<len(arr)-1 and arr[i]==arr[i+1]):
            i+=1
            count+=1
        ans+=arr[i]+str(count)
        i+=1
    return ans

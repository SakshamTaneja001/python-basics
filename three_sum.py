def three_sum(arr):
    arr.sort()
    result=[]
    for k in range(len(arr)-2):
        if k > 0 and arr[k] == arr[k-1]:  # ye add karo
             continue                        # duplicate k skip karo
        i=k+1
        j=len(arr)-1
        while i<j:
             s=arr[i]+arr[j]+arr[k]
             if s==0:
                 result.append([arr[k],arr[i],arr[j]])
                 i+=1
                 j-=1
             elif s<0:
                 i+=1
             else:
                 j-=1
    return result
arr=list(map(int,input("Enter array:").split()))
b=three_sum(arr)
print(b)
                       



    

         
     
    
    
    

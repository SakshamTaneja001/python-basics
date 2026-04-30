def remove_duplicates(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        j+=1
     
    return arr[:i+1]
arr=list(map(int,input("Enter array: ").split()))
arr.sort() 
a=remove_duplicates(arr)
print(a)
                       



    

         
     
    
    
    

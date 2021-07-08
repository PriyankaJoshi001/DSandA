def longestCommonPrefix(strs):
    n=len(strs)
    minlength =0
    minlength = findMinlength(strs,n)
    result =""
    for i in range(minlength):
        current = strs[0][i]
        for j in range(1,n):
            if(strs[j][i]!=current):
                return result
        result = result +current
    return(result)
    
def findMinlength(arr,n):
    min = len(arr[0])
    for i in range(1,n):
        if(len(arr[i])<min):
            min = len(arr[i])
    return(min)

strs=[]
print("Enter the length")
n=int(input())
print("enter the elements")
for i in range(n):
    ele =input()
    strs.append(ele)
print(longestCommonPrefix(strs))



        

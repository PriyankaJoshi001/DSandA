#Shufflr the array
#The array consist of 2n elements in the form [x1,x2,x2....xn , y1,y2,y3.....yn]
#your task is to return the array in the form [x1,y1,x2,y2,x3,y3.......xn,yn]


print("Enter the size of the array")
x= int(input())
nums=[]
print("enter the elements of the array")
for i in range(x):
    ele=int(input())
    nums.append(ele)
n=x//2
l=[]
for i in range(n):
    l.append(nums[i])
    l.append(nums[i+n])
    
print(l)

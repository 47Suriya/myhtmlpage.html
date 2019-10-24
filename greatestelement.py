n=int(input())
set=[]
for i in range(n):
    x=int(input())
    set.append(x)
print(set)

print("Greatest element in the set")
greatest=set[0]
for i in range(1,n):
    if(set[i]>greatest):
        greatest=set[i]
print(greatest)



        
        






















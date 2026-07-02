# num=[0,0,0]
# num_1=[]
# target=[[-1,0,1],[2,-1,1]]
# for i in range(0,len(num)):
#     for j in range(1,len(num)-1):
#       for k in range(2,len(num)):
#         s=num[i]+num[k]+num[j]
#         if s==0:
#             r=[num[i],num[k],num[j]]
#             if r in target:
#               num_1.insert(i,r)
# print(num_1)

num=[0,0,0]
target=1
for i in range(0,len(num)):
    for j in range(1,len(num)):
      for k in range(2,len(num)):
        s=num[i]+num[k]+num[j]
if s==target+1:
    print(s)
elif s==target-1:
   print(s)



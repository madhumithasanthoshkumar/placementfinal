"""name='Madhu'
register_no=712823243036
cgpa=8.94
cgpa_2=
finalclass=4
print(name)
print(register_no)
print(cgpa)
if finalclass==4:
    c=True
if c==True:
    print("YES")
mark=[99,78,86,59,96]
a=50
b=40
print("Addition",a+b)
print("Subtraction",-b)
print("Multiplicaton",a*b)
print("Divition",a/b)
print("Modulus",a%b)
print("Floor division",a//b)
if a==b:
    print("A and B are equal")
else:
        print("A and B are not equal")
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a%=5
print(a)
m=[1,"keerthi",4.7]
print(m)
m.append(5)
print(m)
m.insert(1,30)
print(m)
m.remove(m[2])
print(m)
n=[23,76,85,36]
m.extend(n)
print(m)
o=[54,77,22,65]
p=m+o
print(p)
m[2]=6
print(m)
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print("A",a)
print(a[4:6])
print(b[1:3])
a={"name":"Madhu",'reg':45}
print("A",a)
print(a["name"])
b=(1,2,4,6,7,8)
print(b)
me="madhu"
hi="hi"
print(me*3)
print(hi+me)
print(len(me))
print(me[-1])
print(me.upper())
print(me.lower())
print(me[0])
a_list=[]
for i in range(10):
    a=int(input())
    a_list.append(a)
print("List=",a_list)
max_list=max(a_list)
print("Max:",max_list)
min_list=min(a_list)
print("Min:",min_list)
sum_a=sum(a_list)
print("Sum of list:",sum_a)
average=sum_a/10
print("Average:",average)
no_duplicates=[]
for i in range(0,10):
    if a_list[i] not in no_duplicates:
      no_duplicates.append(a_list[i])
print("After remove duplicates:",no_duplicates)
ascent=no_duplicates.sort()
print("Ascending order:",ascent)
descent=no_duplicates.sort(reverse=True)
print("Descending order:",descent)
tuples=(min_list,max_list,sum_a,average)
print(tuples)
a_list=[]
for i in range(5):
    a=int(input())
    a_list.append(a)
print("List=",a_list)
a_list.insert(3,5)
print(a_list)
a_list.sort()
print(a_list)
b=[4,5,6]
a_list.extend(b)
print(a_list)
print(len(a_list))
mid=len(a_list)//2
a_list.insert(mid,6)
a_list.insert(mid+1,7)
print(a_list)
a_list=[]
for i in range(5):
    a=int(input())
    a_list.append(a)
print("List=",a_list)
arr_list=[[1,2,3],[4,5,6]]
print(arr_list)
print(arr_list)"""
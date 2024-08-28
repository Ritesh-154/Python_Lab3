a=input("enter the string : ")
dic={ }
for i in range(45,90):
    dic[chr(i)]=0
for i in range(90,180):
    dic[chr(i)]=0
for i in a:
    if i in dic:
        dic[i]+=1
for j in dic:
    if dic[j]!=0:
        print(j," - ",dic[j])
    else:
        continue
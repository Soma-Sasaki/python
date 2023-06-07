even=[]
odd=[]

while True:
    a=input("整数を入力してください : ")
    if a != "":
        a=int(a)
        if a%2==0:
            even.append(a)
        else:
            odd.append(a)
    else:
        break

print("偶数は{}\n奇数は{}です".format(even,odd))

even.sort()
odd.sort()

print("偶数は{}\n奇数は{}です".format(even,odd))

Even=set(even)
Odd=set(odd)


print("偶数は{}\n奇数は{}です".format(sorted(Even),sorted(Odd)))

a,b=input().split()
n=int(a+b) #文字列としてaとbを連結した後にint型に変換
if n**(0.5)%1==0: #nが整数であるかどうかの判定
    print('Yes')
else:
    print('No')

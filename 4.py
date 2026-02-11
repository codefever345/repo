def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
n=int(input("Enter num:"))
#Check if the num of terms is valid
if n<=0:
    print("Enter a positive num: ")
else:
    print("fibnocci sequance is :")
    for i in range(n):
        print(fibo(i),end=' ')    
def Fibo(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return (Fibo(num - 2)+ Fibo(num - 1))
num = int(input("Enter the Range : "))
for n in range(0, num):
    print(Fibo(n))
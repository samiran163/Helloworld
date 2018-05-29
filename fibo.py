def fibo(n):
    a=0
    b=1
    for i in range(n):
        a=b
        b=a+b
        print(a,'\n')
        return b
    num=int(input("Enter the value of n: "))
 print(fibo(num))

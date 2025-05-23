print("right pyramid\n")
n=int(input("enter height of pyramid: "))
for i in range(n):
    x = '*' * (i+1)
    print(f'{x:>10}')
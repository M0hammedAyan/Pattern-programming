print("triangular pyramid\n")
n=int(input("enter height of pyramid: "))
for i in range(0 ,n):
    x = '*' * (2 * i + 1)
    print(f'{x:^20}')
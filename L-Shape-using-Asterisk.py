print("L Shape\n")
n = int(input("Enter height of L shape: "))

for i in range(n):
    if i == n - 1:
        print('*' * n)  
    else:
        print('*')    

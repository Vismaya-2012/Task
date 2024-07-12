row=3
col=5
for i in range(3):
    print(" __",end="")
    print("   ",end="")
print()
for i in range(1,col+2):
    for j in range(3):
        if i%2 !=0:
            print('/  ',end="")
            print('\\__',end="")

        else:
            print('\\__',end="")
            print('/  ',end="")
    print()
rows=4
cols=7
for i in range(4):
    print("  __",end="")
    print("   ",end="")
print()
for i in range(1,cols+2):
    for j in range(4):
        if i%2 !=0:
            print('/  ',end="")
            print('\\__',end="")

        else:
            print('\\__',end="")
            print('/  ',end="")
    print()

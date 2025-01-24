"""# vẽ hình chữ N
n = int(input("nhập vào chiều cao của hình: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i==j:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()"""

"""#heart
for i in range(7):
    for j in range(7):
        if (i == 0 and j in (1,2,4,5)) or (i == 1 and j in (0,3,6)) or (i == 2 and j in (0,6)) or (i == 3 and j in (1,5)) or (i == 4 and j in (2,4)) or (i == 5 and j == 3):
            print("*", end="  ")
        else: print(" ", end="  ")
    print()"""


print('\n'.join
      ([''.join
        ([('Merry Christmas '[(x-y)%8 ]
            if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')
               for x in range(-30,30)])
                   for y in range(15,-15,-1)]))
print("Merry Christmas")




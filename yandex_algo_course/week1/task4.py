a = int(input())
b = int(input())
c = int(input())
# Sqrt(-1x+-1)=0
# ax+b>=0 --> x>-b/a
# c>=0
if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if c ** 2 == b:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    x = (c ** 2 - b) / a
    if x % 1 != 0:
        print("NO SOLUTION")
    elif a * x + b < 0:  # x < (-b) / a:
        print("NO SOLUTION")
    else:
        print(int(x))


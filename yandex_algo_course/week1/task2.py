a = int(input())
b = int(input())
c = int(input())

# def check_side(s_check,s1,s2):
#     if s_check>=s1+s2:
#         return 'NO'
#     else:
#         return 'YES'


if a >= b + c:
    ans = "NO"
elif b >= a + c:
    ans = "NO"
elif c >= a + b:
    ans = "NO"
else:
    ans = "YES"
print(ans)

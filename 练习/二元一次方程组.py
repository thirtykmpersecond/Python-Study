A = float(input("输入A："))
B = float(input('输入B：'))
C = float(input('输入C：'))

#计算delta

delta = pow(B, 2) - 4*A*C
if delta < 0 :
    print("无解！")
elif delta == 0 :
    x=B/(-2* A)
    print("x1 = x2 = ", x)
else :
    x1 = (B + delta**0.5) / (-2*A)
    x2 = (B - delta**0.5) / (-2*A)
    print('x1=', x1)
    print('x2=', x2)
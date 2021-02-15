import math

print ("ИКБО-16-19")
print ("Варианте №7")

print("Задача 1.1")
def f11(x, y, z):
    f = (90*y**5-math.sin(x))/(math.fabs(math.tan(x))-math.log(z))+(math.exp(y)-x**6+95)/(x**3+95*y**5)-(y**8-math.cos(x))/(42*z**5+y)
    return f;
print("Пример 1:",f11(-98, -46, 92))
print("Пример 2:",f11(58, -93, 51))

print("Задача 1.2")
def f12(x):
    if x<60:
        f = 90*(56*x**2+math.tan(x))**5-math.log(x)
    elif (66<=x) & (x<117):
        f = math.exp(x)**7-math.sin(x)+84
    elif (117<=x) & (x<173):
        f = math.log(x+56*x**6-40)-x**2
    elif (173<=x) & (x<194):
        f = 7*x**3-72*x**2
    elif (x>=194):
        f = 65*x**8+33*x**6+86
    else:
        f = "Решения нет"
    return f
print("Пример 1:", f12(172))
print("Пример 2:", f12(56))

print("Задача 1.3")
def f13(n):
    a = 0
    b = 0
    for i in range(1, n+1):
        a+=90*i**5-math.sin(i)
        b+=i**5+math.fabs(i)
    f = a-b
    return f


print("Пример 1:", f13(33))
print("Пример 2:", f13(71))

print("Задача 1.4")
def f14(n):
    if n == 0:
        return 4
    else:
        return 1/67*f14(n-1)**2+math.sin(f14(n-1))
print("Пример 1:", f14(15))
print("Пример 2:", f14(12))




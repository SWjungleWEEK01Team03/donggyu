# sol.1
a= input()
b= input()
a = int(a)
b = int(b)

c= a * (b % 10)
d= a * (b//10 % 10)
e= a * (b//100)
print(c)
print(d)
print(e)
print(a*b)

# sol.2
A = int(input())
B = input()

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
print(AxB2, AxB1, AxB0, A*int(B), sep="\n")

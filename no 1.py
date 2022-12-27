def Trapezoid(a,b,f):
    n = 100
    def trapezoid(f,a,b,n=100):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))


for i in range(0,10):
    Trapezoid(i+2,i+4,lambda x: x**2 - 5)
    
for i in range(0,10):
    Trapezoid(i+1,i+3,lambda x: x**4 + 1 )

for i in range(0,10):
    Trapezoid(i+10,i+12,lambda x: x**9 - 2)

for i in range(0,10):
    Trapezoid(i+1,i+2,lambda x: x**7 + 10 )

for i in range(0,10):
    Trapezoid(i+5,i+12,lambda x: 5*x + 8)

for i in range(0,10):
    Trapezoid(i+1,i+2,lambda x: 8*x + 4)

for i in range(0,10):
    Trapezoid(i+2,i+3,lambda x: 2*x + 15)

for i in range(0,10):
    Trapezoid(i+1,i+5,lambda x: 9*x +2)

for i in range(0,10):
    Trapezoid(i+1,i+7,lambda x: 10*x+ 2)

for i in range(0,10):
    Trapezoid(i+1,i+4,lambda x: 11*x+40)

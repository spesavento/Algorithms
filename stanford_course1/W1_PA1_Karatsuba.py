import math

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
#number of digits
n = 64

def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y
    
    #find n (longest number of digits between x and y)
    xstr = str(x)
    ystr = str(y)
    n = max(len(xstr), len(ystr))
    print(n)
    #if n is odd, then subtract 1, else subtracts 0
    n -= n % 2
    
    #10 ** (n/2) for the equation
    mult = 10 ** (n // 2)
    #e.g. 10 ** 2 = 100
    #x = 5678
    #y = 1234
    a, b = divmod(x, mult) #56, 78
    c, d = divmod(y, mult) #12, 34
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    
    #need to calculate (ad + bc)
    adbc = karatsuba(a + b, c + d) - ac - bd 
    
    #x * y = 10^n ac + 10^n/2 (ad + bc) + bd 
    return ((10 ** n) * ac) + mult * adbc + bd
   
res = karatsuba(x, y)
print('%d x %d = %d' % (x, y, res))

#Answer:
#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
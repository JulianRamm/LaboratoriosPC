## Punto 1
def pertFib(n, a=1, b=1):
    if n == 1 or n == 0:
        return True
    next = a + b
    if next > n:
        return False
    elif next == n:
        return True
    else:
        return pertFib(n, b, next)
print(pertFib(14))
## Punto 2
import
def pertSerieC(n):
    if n == 1:
        return True
    elif n :




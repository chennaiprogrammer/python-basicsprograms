"""
n=5
N=(1/2)+(2/3)+(3/4)+(4/5)+(5/6)
"""
import fractions
N=int(input('enter the number:' ))
series=0
for i in range(1,N+1):
    series=series+(i/(i+1))
print(fractions.Fraction(series))

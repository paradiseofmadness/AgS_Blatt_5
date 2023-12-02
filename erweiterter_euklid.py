import random

def erweit_eukl(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        ggt, u, v = erweit_eukl(b % a, a)
        return (ggt, v - (b // a) * u, u)

for _ in range(10):
    a, b = random.randint(2,500), random.randint(2,500)
    ggt, u, v = erweit_eukl(a, b)
    print(f"ggT({a},{b}) = {ggt} = {u*a + v*b} = {u}*{a} + {v}*{b}")

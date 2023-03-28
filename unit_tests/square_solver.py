from typing import List
import math

def solve(a: float, b: float, c: float) -> List[float]: 

    if math.isnan(a) or math.isnan(b) or math.isnan(c):
        raise AttributeError

    epsilon = pow(10, -7)

    if abs(a) < epsilon:
        raise AttributeError
    
    D = pow(b, 2) - 4*a*c    

    if D < 0:
        return []
    
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2*a    
        return [x1, x2]
    
    else:
        return [-b/2*a]
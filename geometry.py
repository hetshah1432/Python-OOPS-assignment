import math

class ShapeCalculator:
    def area(self, a=0, b=None):
        if b is None:
            result = math.pi * a * a
            print(f"Area of Circle with radius {a}: {result:.2f}")
            return result
        else:
            result = a * b
            print(f"Area of Rectangle ({a} x {b}): {result}")
            return result

calc = ShapeCalculator()
calc.area(5)  
calc.area(4, 6)

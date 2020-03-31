from math import sqrt

# quadratic equation formula:
# ax^2 + bx + c = 0
def solveQuadraticEquation(a, b, c):
    if(a == 0):
        # the equation returns imaginary root and infinity
        return("This equation has no solution")

    discriminant = (b*b) - (4*a*c)

    if(discriminant < 0):
        # the equation returns imaginary roots
        return("This equation has no solution")

    rootOne = (-b + sqrt(discriminant)) / (2 * a)
    rootTwo = (-b - sqrt(discriminant)) / (2 * a)
    print("the roots of the equation are:")
    return(rootOne, rootTwo)


if __name__ == "__main__":
    print("please enter a")
    a = int(raw_input())
    print("please enter b")
    b = int(raw_input())
    print("please enter c")
    c = int(raw_input())
    print(solveQuadraticEquation(a, b, c))

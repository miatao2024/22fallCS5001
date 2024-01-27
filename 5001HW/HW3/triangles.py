'''
    CS5001
    Homework 3, 11/03/2022
    Fall 2022
    Minjia Tao
'''

# import turtle
# t = turtle.Turtle()
from turtle import *
t = Turtle()


# H
def draw_triangle(x1, y1, x2, y2, x3, y3):
    h = window_height()
    w = window_width()
    if not(-w/2 < x1 < w/2 and -w/2 < x2 < w/2 and -w/2 < x3 < w/2 and -h/2 < y1 < h/2 and -h/2 < y2 < h/2 and -h/2 < y3 < h/2):
        return False
    else:
        t.speed('normal')
        t.goto(x1, y1)
        t.towards(x2, x2)
        t.forward(distance(x1, y1, x2, y2))
        t.goto(x3, y3)
        t.goto(x1, y1)
        screen = Screen()
        screen.exitonclick()
        return True


# A
def distance(x1, y1, x2, y2):
    side = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return side


# B
def perimeter(x1, y1, x2, y2, x3, y3):
    distance1 = distance(x1, y1, x2, y2)
    distance2 = distance(x1, y1, x3, y3)
    distance3 = distance(x2, y2, x3, y3)
    total_perimeter = float(distance1 + distance2 + distance3)
    return total_perimeter


#C
def area(x1, y1, x2, y2, x3, y3):
    s = float(perimeter(x1, y1, x2, y2, x3, y3) / 2)
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    triangle_area = (s*(s-d1)*(s-d2)*(s-d3))**0.5
    return float(triangle_area)


#D
def approx_equal(d1, d2):
    if -0.001 <= d1 - d2 <= 0.001:
        return True
    else:
        return False


#E
def approx_isosceles(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    if approx_equal(d1, d2) or approx_equal(d1, d3) or approx_equal(d2, d3):#不知道哪里错了
        return True
    else:
        return False


#F
def approx_equilateral(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    if approx_equal(d1, d2) and approx_equal(d1, d3) and approx_equal(d2, d3):#不知道哪里错了
        return True
    else:
        return False


#G
#A
def distance(x1, y1, x2, y2):
    side = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return side


#B
def perimeter(x1, y1, x2, y2, x3, y3):
    distance1 = distance(x1, y1, x2, y2)
    distance2 = distance(x1, y1, x3, y3)
    distance3 = distance(x2, y2, x3, y3)
    total_perimeter = float(distance1 + distance2 + distance3)
    return total_perimeter


#C
def area(x1, y1, x2, y2, x3, y3):
    s = float(perimeter(x1, y1, x2, y2, x3, y3) / 2)
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    triangle_area = (s*(s-d1)*(s-d2)*(s-d3))**0.5
    return float(triangle_area)


#D
def approx_equal(d1, d2):
    return -0.001 <= d1 - d2 <= 0.001

#E
def approx_isosceles(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    return approx_equal(d1, d2) or approx_equal(d1, d3) or approx_equal(d2, d3)#不知

#F
def approx_equilateral(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    return approx_equal(d1, d2) and approx_equal(d1, d3) and approx_equal(d2, d3)


#G
def main():
    numfail = 0
    #Tests for distance(x1, y1, x2, y2)
    #A-a
    print("Test: distance(0, 0, 4, 4)")
    exp = 5.656854249492381
    if exp != distance(0, 0, 4, 4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {distance(0, 0, 4, 4)}")
    print(f"Failed: {numfail}")
    print()
    print()
    
    #A-b
    print("Test: distance(0, 2, 2, 0)")
    exp = 2.8284271247461903
    if exp != distance(0, 2, 2, 0):
        numfail += 1
    print(f"Expected: {exp}, Actual: {distance(0, 2, 2, 0)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #A-c
    print("Test: distance(0, 0, -4, -4)")
    exp = 5.656854249492381
    if exp != distance(0, 0, -4, -4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {distance(0, 0, -4, -4)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #A-d
    print("Test: distance(0, 2, 2, 0)")
    exp = 1.0
    if exp != distance(0, 2, 2, 0):
        numfail += 1
    print(f"Expected: {exp}, Actual: {distance(0, 2, 2, 0)}")
    print(f"Failed: 1")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for perimeter(x1, y1, x2, y2, x3, y3)
    #B-a
    draw_triangle(0, 0, 0, 2, 2, 2)
    print("Test: perimeter(0, 0, 0, 2, 2, 2)")
    exp = 6.82842712474619
    if exp != perimeter(0, 0, 0, 2, 2, 2):
        numfail += 1
    print(f"Expected: {exp}, Actual: {perimeter(0, 0, 0, 2, 2, 2)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #B-b
    draw_triangle(0, 0, 6, 0, 3, 5.196152422706632)
    print("Test: perimeter(0, 0, 6, 0, 3, 5.196152422706632)")
    exp = 18.0
    if exp != perimeter(0, 0, 6, 0, 3, 5.196152422706632):
        numfail += 1
    print(f"Expected: {exp}, Actual: {perimeter(0, 0, 6, 0, 3, 5.196152422706632)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #B-c
    draw_triangle(0, 0, 0, -2, 2, 2)
    print("Test: perimeter(0, 0, 0, -2, 2, 2)")
    exp = 9.30056307974577
    if exp != perimeter(0, 0, 0, -2, 2, 2):
        numfail += 1
    print(f"Expected: {exp}, Actual: {perimeter(0, 0, 0, -2, 2, 2)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #B-d
    draw_triangle(0, 0, 0, 2, 2, 2)
    print("Test: perimeter(0, 0, 0, 2, 2, 2)")
    exp = 1.0
    if exp != perimeter(0, 0, 0, 2, 2, 2):
        numfail += 1
    print(f"Expected: {exp}, Actual: {perimeter(0, 0, 0, -2, 2, 2)}")
    print(f"Failed: 1")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for area(x1, y1, x2, y2, x3, y3)
    #C-a
    draw_triangle(0, 0, 3, 0, 0, 4)
    print("Test: area(0, 0, 3, 0, 0, 4)")
    exp = 6.0
    if exp != area(0, 0, 3, 0, 0, 4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {area(0, 0, 3, 0, 0, 4)}")
    print(f"Failed: {numfail}")
    print()
    print()

    # C-b
    draw_triangle(-3, 0, 3, 0, 0, 4)
    print("Test: area(-3, 0, 3, 0, 0, 4)")
    exp = 12.0
    if exp != area(-3, 0, 3, 0, 0, 4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {area(-3, 0, 3, 0, 0, 4)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #C-c
    draw_triangle(0, 0, 3, 0, 0, 4)
    print("Test: area(0, 0, 3, 0, 0, 4)")
    exp = 6.0
    if exp != area(0, 0, 3, 0, 0, 4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {area(0, 0, 3, 0, 0, 4)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #C-d
    draw_triangle(-3, 0, 3, 0, 0, 4)
    print("Test: area(-3, 0, 3, 0, 0, 4)")
    exp = 13.0
    if exp != area(-3, 0, 3, 0, 0, 4):
        numfail += 1
    print(f"Expected: {exp}, Actual: {area(-3, 0, 3, 0, 0, 4)}")
    print(f"Failed: {numfail}")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for approx_equal(d1, d2)
    #D-a
    print("Test: approx_equal(1, 1.001)")
    exp = True
    if exp != approx_equal(1, 1.001):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equal(1, 1.001)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #D-b
    print("Test: approx_equal(5.7, 5.71)")
    exp = False
    if exp != approx_equal(5.7, 5.71):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equal(5.7, 5.71)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #D-c
    print("Test: approx_equal(-5.7, -5.71)")
    exp = False
    if exp != approx_equal(-5.7, -5.71):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equal(-5.7, -5.71)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #D-d
    print("Test: approx_equal(5.7, 5.71)")
    exp = True
    if exp != approx_equal(5.7, 5.71):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equal(-5.7, -5.71)}")
    print(f"Failed: {numfail}")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for approx_isosceles(x1, y1, x2, y2, x3, y3)
    #E-a
    draw_triangle(0, 0, 1, 0, 1, 1.0005)
    print("Test: approx_isosceles(0, 0, 1, 0, 1, 1.0005)")
    exp = True
    if exp != approx_isosceles(0, 0, 1, 0, 1, 1.0005):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_isosceles(0, 0, 1, 0, 1, 1.0005)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #E-b
    draw_triangle(0, 0, 1, 0, 1, 0.95)
    print("Test: approx_isosceles(0, 0, 1, 0, 1, 0.95)")
    exp = False
    if exp != approx_isosceles(0, 0, 1, 0, 1, 0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_isosceles(0, 0, 1, 0, 1, 0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #E-c
    draw_triangle(0, 0, 1, 0, -1, -0.95)
    print("Test: approx_isosceles(0, 0, 1, 0, -1, -0.95)")
    exp = False
    if exp != approx_isosceles(0, 0, 1, 0, -1, -0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_isosceles(0, 0, 1, 0, -1, -0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #E-d
    draw_triangle(0, 0, 1, 0, 1, 0.95)
    print("Test: approx_isosceles(0, 0, 1, 0, 1, 0.95)")
    exp = True
    if exp != approx_isosceles(0, 0, 1, 0, 1, 0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_isosceles(0, 0, 1, 0, 1, 0.95)}")
    print(f"Failed: {numfail}")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for approx_equilateral(x1, y1, x2, y2, x3, y3) 
    #F-a
    draw_triangle(1, 3, -2.0, 7, 2.964, 7.598)
    print("Test: approx_equilateral(1, 3, -2.0, 7, 2.964, 7.598)")
    exp = True
    if exp != approx_equilateral(1, 3, -2.0, 7, 2.964, 7.598):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equilateral(1, 3, -2.0, 7, 2.964, 7.598)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #F-b
    draw_triangle(3, 1, 1, 0, 1, 0.95)
    print("Test: approx_equilateral(3, 1, 1, 0, 1, 0.95)")
    exp = False
    if exp != approx_equilateral(3, 1, 1, 0, 1, 0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equilateral(3, 1, 1, 0, 1, 0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #F-c
    draw_triangle(3, 1, 1, 0, -1, -0.95)
    print("Test: approx_equilateral(3, 1, 1, 0, -1, -0.95)")
    exp = False
    if exp != approx_equilateral(3, 1, 1, 0, -1, -0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equilateral(3, 1, 1, 0, -1, -0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #F-d
    draw_triangle(3, 1, 1, 0, 1, 0.95)
    print("Test: approx_equilateral(3, 1, 1, 0, 1, 0.95)")
    exp = True
    if exp != approx_equilateral(3, 1, 1, 0, 1, 0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {approx_equilateral(3, 1, 1, 0, 1, 0.95)}")
    print(f"Failed: {numfail}")
    print(f"Total Failed: {numfail}")
    print()
    print()


    #Tests for draw_triangle(x1, y1, x2, y2, x3, y3)
    #H-a
    print("Test: draw_triangle(3, 1, 1, 0, 1, 0.95)")
    exp = True
    if exp != approx_equilateral(3, 1, 1, 0, 1, 0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {draw_triangle(3, 1, 1, 0, 1, 0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()
    
    #H-b
    print("Test: draw_triangle(3, 1, 1, 0, -1, -0.95)")
    exp = True
    if exp != approx_equilateral(3, 1, 1, 0, -1, -0.95):
        numfail += 1
    print(f"Expected: {exp}, Actual: {draw_triangle(3, 1, 1, 0, -1, -0.95)}")
    print(f"Failed: {numfail}")
    print()
    print()

    #H-c
    print("Test: draw_triangle(1, 3, -2.0, 7, 2.964, 7.598)")
    exp = True
    if exp != draw_triangle(1, 3, -2.0, 7, 2.964, 7.598):
        numfail += 1
    print(f"Expected: {exp}, Actual: {draw_triangle(1, 3, -2.0, 7, 2.964, 7.598)}")
    print(f"Failed: {numfail}")
    print()
    print()




# I
def equitri(leng):
    t.speed(6)
    t.forward(leng)
    t.right(120)
    t.forward(leng)
    t.right(120)
    t.forward(leng)


def cool_tri(counter):
    i = 0
    while i < counter:
        equitri(45 + 9 * i)
        t.right(60)
        i += 1
    #t.exitonclick()


if __name__ == "__main__":
    main()
    if draw_triangle(0, 0, 100, 100, 0, 0):
        print(f"The area is {area(0, 0, 100, 100, 0, 0)}")
        print(f"The perimeter is {perimeter(0, 0, 100, 100, 0, 0)}")
        if approx_isosceles(0, 0, 100, 100, 0, 0):
            print(f"The triangle is isosceles.")
        else:
            print(f"The triangle is not isosceles.")
    print(draw_triangle(0, 0, 100, 100, 200, 200))
    cool_tri(6)


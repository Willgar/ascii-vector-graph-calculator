import sympy
from sympy import *
x, y = sympy.symbols('x y')

def determine_value(xi, yj):
    #print(xi,yj)
    if (xi > 0 and yj > 0) or (xi < 0 and yj < 0):
        return "/"
    elif (xi > 0 and yj < 0) or (xi < 0 and yj > 0):
        return "\\"
    elif xi == 0 and yj != 0:
        return "-"
    elif xi != 0 and yj == 0:
        return "|"
    else:
        return ""
class Square:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.value=determine_value(x1,y1)

exp = []
exp.append([sympy.sqrt(x*x),sympy.sqrt(y*y)])
exp.append([sin(x),sin(-y)*sin(-y)])
exp.append([cos(x),cos(-y)*cos(-y)])
exp.append([sin(x),sin(-y)])

def main():
    gridsize = 100
    for k in range(len(exp)):
        grid = []
        for i in range(gridsize):
            grid.append([])
            for j in range(gridsize):
                val1 = exp[k][0].subs(x, (i-(gridsize/2)))
                val2 = exp[k][1].subs(y, (j-(gridsize/2)))
                grid[i].append(Square(val1,val2))
                print(grid[i][j].value, end="")
            print("")
        print("\n\n")

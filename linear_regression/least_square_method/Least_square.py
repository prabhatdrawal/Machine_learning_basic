def calculating_b(n,sum_xy,sum_x,sum_y,sum_x2):
    b = ( n*sum_xy - sum_x*sum_y )/(n*sum_x2 - pow(sum_x,2))
    return b

def calculating_a(n,sum_y,sum_x,b):
    a = (sum_y/n)-((b*sum_x)/n)
    return a 

n = float(input("enter the total number of values:"))
sum_x = float(input("enter the total summation  of x values:"))
sum_y = float(input("enter the total summation of y values:"))
sum_xy = float(input("enter the total summation of xy values:"))
sum_x2 = float(input("enter the total summation  of x2 values:"))

b_calculation = calculating_b(n,sum_xy,sum_x,sum_y,sum_x2)
a_calculation = calculating_a(n,sum_y,sum_x,b_calculation)

print("the equation obatined is : y =%f+%fx" %(a_calculation,b_calculation))


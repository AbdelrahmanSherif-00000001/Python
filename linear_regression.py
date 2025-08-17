# import numpy as np 
# import matplotlib.pyplot as plt

# #we will calculate mean of x and y as we will need them in calculating SSxy and SSxx, also to calculate B0"Bias".
# #we need SSxy"sum of cross deviation of x and y" and SSxx"sum squared deviation of X" to calculate B1"Slope".
# #n is used to know number of elements "data" we will work for and will be important in calculations as well.
# #we will use B1 to calculate the B0.


# def calc_slope_and_bias(x,y):
#     n = np.size(x)

#     mX = np.mean(x)
#     mY = np.mean(y)

#     SSxy = np.sum(x*y) - n*mX*mY
#     SSxx = np.sum(x*x) - n*mX*mX

#     B1 = SSxy / SSxx
#     B0 = mY - B1*mX 

#     return(B0,B1)

# def plot_regression_line(x,y,b):
#     plt.scatter(x, y, color="m", marker="s", s = 30)
#     yPredicted = b[0] + b[1]*x

#     plt.plot(x,yPredicted,color="g")

#     plt.xlabel('X')
#     plt.ylabel('Y')

# def main():
#     x = np.array([1,2,3,4,5,6])
#     y = np.array([2,4,6,8,10,12])

#     b = calc_slope_and_bias(x,y)

#     plot_regression_line(x,y,b)
#     plt.show()
#     main()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/abdel/Downloads/Salary_Data.csv")

x = data['YearsExperience'].values
y = data['Salary'].values

def calc_B0_and_B1(x,y):
    n = np.size(x)

    mX = np.mean(x)
    mY = np.mean(y)

    SSxy = np.sum(x*y) - n*mX*mY
    SSxx = np.sum(x*x) - n*mX*mX

    B1 = SSxy / SSxx
    B0 = mY - B1*mX
    
    return(B0,B1)

def plot_LR(x,y,b):
    plt.scatter(x,y,color="m",marker="^")
    y_predicted = b[0] + b[1]*x
    plt.plot(x,y_predicted)
    plt.xlabel("X")
    plt.ylabel("Y")

def predict_Y(feature, b):
    Y_predictd = b[0] + b[1]*feature
    return Y_predictd

def main():
    b = calc_B0_and_B1(x,y)
    plot_LR(x,y,b)
    plt.show()
    print(predict_Y(5.1,b))
    
main()
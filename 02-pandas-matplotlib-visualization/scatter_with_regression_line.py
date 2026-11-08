## line , bar, scatter,histogram,pie
##     scatter
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter
import numpy as np
x = [1,2,3,4,5]
y = [3,4,6,8,10]

## fit a linear regression line to the data

slope, intercept = np.polyfit(x, y, 1)
print(f"Slope: {slope}, Intercept: {intercept}")
fit_line = [slope * i + intercept for i in x] # y  = m*i + c


plt.scatter(x, y,color = "red", label='Line')
plt.plot(x, fit_line, color='blue', label='Fitted Line')

plt.show()

# plt.line (x, y, color='red', label='Line')
# plt.title("Scatter Plot with Line")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

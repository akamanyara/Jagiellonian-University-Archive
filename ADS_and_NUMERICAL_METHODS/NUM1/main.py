import numpy as np
import matplotlib.pyplot as plt

# function for f(x) = sin(x^3)
def function(x):
    return np.sin(x**3)

# derivative of f'(x)
def derivative(x):
    return 3*(x**2)*np.cos(x**3)

# diff appro a)
def forward_diff_appr(h, x):
    return (function(x + h) - function(x)) / h

# diff appro b)
def central_diff_appr(h, x):
    return (function(x + h) - function(x - h)) / (2 * h)

# error calculation
def error(appr, h, x, dtype):
    a = appr(h.astype(dtype), x.astype(dtype))
    b = derivative(x.astype(dtype))
    return np.abs(a - b)

# defining the x and h values 
x = np.array([0.2])

h_value64 = np.logspace(-18, 0, 1000).astype(np.float64)
h_value32 = h_value64.astype(np.float32)

# error store arrays
forward_64 = []
central_64 = []

forward_32 = []
central_32 = []

# errors for each h
for h in h_value64:
    forward_64.append(error(forward_diff_appr, h, x, np.float64))
    central_64.append(error(central_diff_appr, h, x, np.float64))

for h in h_value32:
    forward_32.append(error(forward_diff_appr, h, x, np.float32))
    central_32.append(error(central_diff_appr, h, x, np.float32))

# now the graphs 
plt.figure(figsize = (10,6))

# for float64
plt.subplot(2, 1, 1)
plt.loglog(h_value64, forward_64, label="Forward Diff. Error", color='blue')
plt.loglog(h_value64, central_64, label="Central Diff. Error", color='red')

plt.title("Forward and Central Difference Errors for float64")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-12,1)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()

# for float32 
plt.subplot(2, 1, 2)
plt.loglog(h_value32, forward_32, label="Forward Diff. Error", color='blue')
plt.loglog(h_value32, central_32, label="Central Diff. Error", color='red')

plt.title("Forward and Central Difference Errors for float32")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-8, 1)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# THIS PROGRAMM IS JUST ABOUT EXAMPLES OF OTHER FUNCTIONS
# example functions: e^(x^2) and the same with diff point

def function(x):
    return np.exp(x**2)

def derivative(x):
    return 2 * x * (np.exp(x**2))

def forward_diff_appr(h, x):
    return (function(x + h) - function(x)) / h

def central_diff_appr(h, x):
    return (function(x + h) - function(x - h)) / (2 * h)

def error(appr, h, x, derivative, dtype):
    a = appr(h.astype(dtype), x.astype(dtype))
    b = derivative(x.astype(dtype))
    return np.abs(a - b)

x1 = np.array([0.2])

#other point
x2 = np.array([2.0])

h_value64 = np.logspace(-18, 0, 1000).astype(np.float64)
h_value32 = h_value64.astype(np.float32)

def calculate_errors_forward(derivative, h_values, x, dtype):
    forward_errors = []
    
    for h in h_values:
        forward_errors.append(error(forward_diff_appr, h, x, derivative, dtype))
    
    return forward_errors


def calculate_errors_central(derivative, h_values, x, dtype):
    central_errors = []
    
    for h in h_values:
        central_errors.append(error(central_diff_appr, h, x, derivative, dtype))
    
    return central_errors

fun1_forward64 = calculate_errors_forward(derivative, h_value64, x1, np.float64)
fun1_central64 = calculate_errors_central(derivative, h_value64, x1, np.float64)

fun1_forward32 = calculate_errors_forward(derivative, h_value32, x1, np.float32)
fun1_central32 = calculate_errors_central(derivative, h_value32, x1, np.float32)

fun2_forward64 = calculate_errors_forward(derivative, h_value64, x2, np.float64)
fun2_central64 = calculate_errors_central(derivative, h_value64, x2, np.float64)

fun2_forward32 = calculate_errors_forward(derivative, h_value32, x2, np.float32)
fun2_central32 = calculate_errors_central(derivative, h_value32, x2, np.float32)

# now for the plots
plt.figure(figsize=(12, 10))

#1 x=0.2 and float64
plt.subplot(2, 1, 1)
plt.loglog(h_value64, fun1_forward64, label="Forward Diff. Error", color='blue')
plt.loglog(h_value64, fun1_central64, label="Central Diff. Error", color='red')

plt.title("x=0.2 errors for exp., float64")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-12,1e+3)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()

#2 x=0.2 and float32
plt.subplot(2, 1, 1)
plt.loglog(h_value32, fun1_forward32, label="Forward Diff. Error", color='blue')
plt.loglog(h_value32, fun1_central32, label="Central Diff. Error", color='red')

plt.title("x=0.2 errors for exp., float32")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-12,1e+3)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()

#3 x=0.5 and float64
plt.subplot(2, 1, 1)
plt.loglog(h_value64, fun2_forward64, label="Forward Diff. Error", color='blue')
plt.loglog(h_value64, fun2_central64, label="Central Diff. Error", color='red')

plt.title("x=2.0 errors for exp., float64")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-12,1e+3)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()

#4 x=0.5 and float32
plt.subplot(2, 1, 1)
plt.loglog(h_value32, fun2_forward32, label="Forward Diff. Error", color='blue')
plt.loglog(h_value32, fun2_central32, label="Central Diff. Error", color='red')

plt.title("x=2.0 errors for exp., float32")
plt.xlabel("h values")
plt.ylabel("Error |D_h f(x) - f'(x)|")

plt.ylim(1e-12,1e+3)
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()

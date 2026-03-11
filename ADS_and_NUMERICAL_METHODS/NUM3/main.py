import matplotlib.pyplot as plt
import time
from functools import reduce

# LU distribution function
def LU(n):

    matrix = []
    matrix.append([0] + [0.3] * (n - 1))  # under diag
    matrix.append([1.01] * n)  # diagonal
    matrix.append([0.2 / i for i in range(1, n)] + [0])  # 1 up diag
    matrix.append([0.15 / (i * i * i) for i in range(1, n - 1)] + [0] + [0])  # 2 up diag

    # vector
    x = list(range(1, n + 1))

    # LU factorization ( all 4 diag )
    for i in range(1, n):
        if i < n - 1:
            matrix[0][i] /= matrix[1][i - 1]
            matrix[1][i] -= matrix[0][i] * matrix[2][i - 1]
            matrix[2][i] -= matrix[0][i] * matrix[3][i - 1]
        elif i == n - 1:
            matrix[0][i] /= matrix[1][i - 1]
            matrix[1][i] -= matrix[0][i] * matrix[2][i - 1]

    # solve LUx = b equation
    for i in range(1, n):
        x[i] -= matrix[0][i] * x[i - 1]

    x[n - 1] /= matrix[1][n - 1]
    x[n - 2] = (x[n - 2] - matrix[2][n - 2] * x[n - 1]) / matrix[1][n - 2]

    for i in range(n - 3, -1, -1):
        x[i] = (x[i] - matrix[3][i] * x[i + 2] - matrix[2][i] * x[i + 1]) / matrix[1][i]

    # determinant 
    det = reduce(lambda a, b: a * b, matrix[1])

    return x, det

N = 300

repeats = 150
times = []
sizes = list(range(5, N + 1, 1))

result, determinant = LU(N)
print("Determinant:", determinant)
print("Result:", result)

# meassure time for different N sizes 
for n in sizes:
    repeat_times = []
    for _ in range(repeats):
        start_time = time.time()
        LU(n)
        end_time = time.time()
        repeat_times.append(end_time - start_time)

    avg_time = sum(repeat_times) / repeats
    times.append(avg_time)

# time graphs 
plt.figure(figsize=(12, 6))
plt.plot(sizes, times, marker='o', linestyle='-', color="r")
plt.xlabel('Matrix Size')
plt.ylabel('Average working time')
plt.title('Working time of LU function')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt # for graphs 
import numpy as np # for testing the solution !
import time # for time measurement

def test_solution(n):
    A = np.diag([4] * n) + np.diag([2] * (n - 1), 1) + np.ones((n, n))
    b = np.full(n,2)
    return np.linalg.solve(A, b)

def sherman_morrison(M, b, n):
    y = []
    # vectors that help with: Az = b and Aq = u 
    z = [0] * n
    q = [0] * n

    z[n - 1] = b[n - 1] / M[0][n - 1]
    q[n - 1] = 1 / M[0][n - 1]

    # backwards subs. ( count z and q values )
    for i in range(n - 2, -1, -1):
        z[i] = (b[i] - M[1][i] * z[i + 1]) / M[0][i]
        q[i] = (1 - M[1][i] * q[i + 1]) / M[0][i]

    # part with v^T
    delta = sum(z) / (1 + sum(q))

    # results corrections
    for i in range(n):
        y.append(z[i] - q[i] * delta)

    return y

def measure_time_MN(timers,N_values,N):
    for N in N_values:
        start_time = time.time()
        matrix = [[4] * N, [2] * (N - 1) + [0]]
        b = [2] * N
        sherman_morrison(matrix, b, N)
        timers.append((time.time() - start_time))


def measure_time_Numpy(timers,N_values,N):
    for N in N_values:
        start_time = time.time()
        A = np.diag([4] * N) + np.diag([2] * (N - 1), 1) + np.ones((N, N))
        b = [2] * N
        np.linalg.solve(A, b)
        timers.append((time.time() - start_time))

n = 120
M = []
M.append([4] * n)
M.append([2] * (n - 1) + [0])
b = [2] * n

morrison_custom = sherman_morrison(M, b, n)
print("Sherman-morrison test results:")
print(morrison_custom)

numpy_results = test_solution(n)
print("Numpy test results:")
print(numpy_results)

# to see the O(n)
N_values_sm_solo = range(10, 1000000, 10000) 
timers_sm_solo = []
measure_time_MN(timers_sm_solo, N_values_sm_solo,n)

# for comparision
N_values_sm = range(10, 10000, 500)
timers_sm = []
measure_time_MN(timers_sm,N_values_sm,n)

N_values_num = range(10, 10000, 500)
timers_num = []
measure_time_Numpy(timers_num,N_values_num,n)

# comparision plot
plt.plot(N_values_sm, timers_sm,label="Sherman-Morrison algorithm")
plt.plot(N_values_num, timers_num,label="Numpy solution")
plt.grid(True)
plt.xlabel("Matrix size N")
plt.ylabel("Results time [s]")
plt.title("Time of N sized function")
plt.legend()
plt.show()

# O(n) plot
plt.plot(N_values_sm_solo, timers_sm_solo,label="Sherman-Morrison algorithm")
plt.grid(True)
plt.xlabel("Matrix size N")
plt.ylabel("Results time [s]")
plt.title("Time of N sized function")
plt.legend()
plt.show()
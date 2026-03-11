import numpy as np
import matplotlib.pyplot as plt

def create_matrix(N, d):
    matrix = np.zeros((5, N))
    matrix[2, :] = d      # main diag
    matrix[1, 1:] = 0.5   # 1st up diag
    matrix[0, 2:] = 0.1   # 2nd up diag
    matrix [3, :-1] = 0.5 # 1st under diag
    matrix[4, :-2] = 0.1  # 2nd under diag
    return matrix

# function to multiply matrix by a vector x
def multiplier(matrix, x):
    N = len(x)
    result = np.zeros_like(x)
    result += matrix[2] * x  # main diag
    result[1:] += matrix[1, 1:] * x[:-1]  # 1st up diag
    result[2:] += matrix[0, 2:] * x[:-2]  # 2nd up diag
    result[:-1] += matrix[3, :-1] * x[1:] # 1st under diag
    result[:-2] += matrix[4, :-2] * x[2:] # 2nd under diag
    return result

# Jacobi method
def jacobi(matrix, b, x0, max_iterations, stop):
    diag_inversed = 1.0 / matrix[2] 
    x = x0.copy()
    errors = []

    for _ in range(max_iterations):
        R_x = multiplier(matrix, x) - matrix[2] * x  # R * x
        x_new = diag_inversed * (b - R_x)
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < stop:
            break
        x = x_new
    
    return x, errors

# Gauss-Seidel method
def gauss_seidel(matrix, b, x0, max_iterations, stop):
    x = x0.copy()
    N = len(b)
    errors = []

    for _ in range(max_iterations):
        x_old = x.copy()
        
        for i in range(N):
            sum1 = 0.0
            sum2 = 0.0

            if i > 0:
                sum1 = matrix[3, i-1] * x[i-1]  # 1st under diag
            if i > 1:
                sum1 += matrix[4, i-2] * x[i-2]  # 2nd under diag
            if i < N-1:
                sum2 = matrix[1, i+1] * x[i+1]  # 1st up diag
            if i < N-2:
                sum2 += matrix[0, i+2] * x[i+2]  # 2nd up diag
            x[i] = (b[i] - sum1 - sum2) / matrix[2, i]

        error = np.linalg.norm(x - x_old, ord=np.inf)
        errors.append(error)
        if error < stop:
            break

    return x, errors

N = 200  
b = np.arange(1, N + 1)
stop = 1e-12  # stop condition
max_iterations = 400

results = {}
# for starting point: vector zero x0 
for d in [0.5, 2.0, 4.0, 8.0, 16.0]: 
    matrix = create_matrix(N, d)
    x_exact = np.linalg.solve(np.diag(matrix[2]) +
                              np.diag(matrix[1,1:], 1) +
                              np.diag(matrix[3,:-1], -1) +
                              np.diag(matrix[0,2:], 2) +
                              np.diag(matrix[4,:-2], -2), b)
    
    x0 = np.zeros(N)  # starting point: vector zero

    x_jacobi, errors_jacobi = jacobi(matrix, b, x0, max_iterations, stop)
    
    x_gs, errors_gs = gauss_seidel(matrix, b, x0, max_iterations, stop)

    results[d] = {
        "x_exact": x_exact,
        "x_jacobi": x_jacobi,
        "x_gs": x_gs,
        "errors_jacobi": errors_jacobi,
        "errors_gs": errors_gs,
    }

    plt.figure(figsize=(12, 6))
    plt.plot(errors_jacobi, label="Jacobi", marker="o", markersize=3)
    plt.plot(errors_gs, label="Gauss-Seidel", marker="s", markersize=3)
    plt.yscale("log")
    plt.title(f"Zbieżność metod iteracyjnych dla d = {d} i pkt. start w zerowym wektorze")
    plt.xlabel("Liczba iteracji")
    plt.ylabel("Error")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"--- dla x0 i d = {d} ---")
    print(f"Rozwiązanie dokładne:\n{x_exact}")
    print(f"Rozwiązanie Jacobiego:\n{x_jacobi}")
    print(f"Rozwiązanie Gaussa-Seidela:\n{x_gs}")
    print("-------------------------------------")
    print(f"Błąd końcowy Jacobiego: {errors_jacobi[-1]}")
    print(f"Błąd końcowy Gaussa-Seidela: {errors_gs[-1]}")

# for starting point: random vector 
for d in [0.5, 2.0, 8.0]: 
    matrix = create_matrix(N, d)
    x_exact = np.linalg.solve(np.diag(matrix[2]) +
                              np.diag(matrix[1,1:], 1) +
                              np.diag(matrix[3,:-1], -1) +
                              np.diag(matrix[0,2:], 2) +
                              np.diag(matrix[4,:-2], -2), b)
    
    x1 = np.random.rand(N) * 2  # starting poin: random vector

    x_jacobi, errors_jacobi = jacobi(matrix, b, x1, max_iterations, stop)
    
    x_gs, errors_gs = gauss_seidel(matrix, b, x1, max_iterations, stop)

    results[d] = {
        "x_exact": x_exact,
        "x_jacobi": x_jacobi,
        "x_gs": x_gs,
        "errors_jacobi": errors_jacobi,
        "errors_gs": errors_gs,
    }

    plt.figure(figsize=(12, 6))
    plt.plot(errors_jacobi, label="Jacobi", marker="o", markersize=3)
    plt.plot(errors_gs, label="Gauss-Seidel", marker="s", markersize=3)
    plt.yscale("log")
    plt.title(f"Zbieżność metod iteracyjnych dla d = {d} i pkt. start w losowym wektorze")
    plt.xlabel("Liczba iteracji")
    plt.ylabel("Error")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"--- dla x1 i d = {d} ---")
    print(f"Rozwiązanie dokładne:\n{x_exact}")
    print(f"Rozwiązanie Jacobiego:\n{x_jacobi}")
    print(f"Rozwiązanie Gaussa-Seidela:\n{x_gs}")
    print("-------------------------------------")
    print(f"Błąd końcowy Jacobiego: {errors_jacobi[-1]}")
    print(f"Błąd końcowy Gaussa-Seidela: {errors_gs[-1]}")

    
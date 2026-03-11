import numpy as np

# create our matrixes
A1 = np.array ([
    [5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064],
    [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
    [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
    [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
    [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]
])

A2 = np.array ([
    [5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547],
    [1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433],
    [0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185],
    [-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573],
    [0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695]
])

b = np.transpose(np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006]))

# let's find the condition numbers for those matrixes - we will call it by kappa1 and kappa2
# kappa = max(eigen value) / min( eigen value )

# first let's count our eigen vaklues
eigenvalue_A1 = np.linalg.eigvals(A1)
eigenvalue_A2 = np.linalg.eigvals(A2)

# now we move to finding our kappa values 
kappa1 = max(abs(eigenvalue_A1)) / min(abs(eigenvalue_A1))
kappa2 = max(abs(eigenvalue_A2)) / min(abs(eigenvalue_A2))

# let's count the Ay = b for both our matrixes
y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)

# now i want to create the randomized delta b to count our disturbed value 
np.random.seed(42)
delta_b = np.random.normal(0, 1, b.shape) # this will create vector delta_b similiar to b vector
delta_b = delta_b / np.linalg.norm(delta_b) * 1e-6 # scale to our example norm 10^-6

disturbed_b = b + delta_b

# Ay = b + delta_b
dis_y1 = np.linalg.solve(A1, disturbed_b)
dis_y2 = np.linalg.solve(A2, disturbed_b)

# lastly analyse the differences between those two 
diff_A1 = np.linalg.norm(y1 - dis_y1)
diff_A2 = np.linalg.norm(y2 - dis_y2)

# print our answer now ( i will comeback to polish lang for better report analysis )
print("ROZWIAZANIA DLA MACIERZY A1")
print("Rozwiazanie dla rownania Ay = b:", "\n", y1)
print("Rozwiazanie dla rownania Ay = b + ∆b:", "\n", dis_y1)
print("Z obu równań wychodzi nam roznica rowna:", "\n", diff_A1)
print("Wskaznik uwarunkowania macierzy A1 to:", kappa1)

print("\n\n")

print("ROZWIAZANIA DLA MACIERZY A2")
print("Rozwiazanie dla rownania Ay = b:", "\n", y2)
print("Rozwiazanie dla rownania Ay = b + ∆b:", "\n", dis_y2)
print("Z obu równań wychodzi nam roznica rowna:", "\n", diff_A2)
print("Wskaznik uwarunkowania macierzy A2 to:", kappa2)
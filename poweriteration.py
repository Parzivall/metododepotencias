import numpy as np

def power_iteration(A, num_simulations: int):
    # Elegimos un vector aleatorio
    # Es Ortogonal
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)

        # Calcula la norma
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k

power_iteration(np.array([[0.5, 0.5], [0.2, 0.8]]), 10)

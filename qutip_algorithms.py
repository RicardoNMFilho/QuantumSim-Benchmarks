from qutip import basis, Qobj
from qutip import tensor, sigmaz, sigmax, mesolve, identity
from qutip import qeye

import numpy as np
from numpy import pi

# Funções Auxiliares

def qft_matrix(n):
        N = 2**n
        matrix = np.zeros((N, N), dtype=complex)
        for i in range(N):
            for j in range(N):
                matrix[i, j] = np.exp(2j * np.pi * i * j / N) / np.sqrt(N)
        return Qobj(matrix)


# Funções Algoritmos Quânticos

def qft_qutip_sim(n_qubits):

    index = 2**(n_qubits - 1)
    input_state = basis(2**n_qubits, index)
    qft = qft_matrix(n_qubits)
    output = qft * input_state
    return output.full().flatten()


def schrodinger_qutip_sim(n_qubits, t=1.0, omega=1.0):

    H = sum([omega * tensor(
        *[sigmaz() if i == j else identity(2) for i in range(n_qubits)]
    ) for j in range(n_qubits)])

    state_list = [basis(2, 1 if i == 0 else 0) for i in range(n_qubits)]
    psi0 = tensor(state_list)

    result = mesolve(H, psi0, [t], [], [])
    return result.states[-1].full().flatten()


def qaoa_qutip_sim(n_qubits, p=1, gamma=0.5, beta=0.5):

    plus = (basis(2, 0) + basis(2, 1)).unit()
    psi = tensor([plus] * n_qubits)

    def rx(theta, wire):
        op_list = [sigmax() if i == wire else qeye(2) for i in range(n_qubits)]
        return (-1j * theta / 2 * tensor(op_list)).expm()

    def rz(theta, wire):
        op_list = [sigmaz() if i == wire else qeye(2) for i in range(n_qubits)]
        return (-1j * theta / 2 * tensor(op_list)).expm()

    def zz(theta, i, j):
        op_list = []
        for k in range(n_qubits):
            if k == i or k == j:
                op_list.append(sigmaz())
            else:
                op_list.append(qeye(2))
        return (-1j * theta * tensor(op_list)).expm()

    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            psi = zz(gamma, i, j) * psi

    for i in range(n_qubits):
        psi = rx(2 * beta, i) * psi

    return psi.full().flatten()
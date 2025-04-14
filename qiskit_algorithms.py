from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from numpy import pi

def qft_qiskit_sim(n_qubits):

    qc = QuantumCircuit(n_qubits)
    qc.x(0)

    for i in range(n_qubits):
        qc.h(i)
        for j in range(i+1, n_qubits):
            qc.cp(pi / 2**(j - i), j, i)
    for i in range(n_qubits // 2):
        qc.swap(i, n_qubits - i - 1)

    qc.save_statevector()
    sim = Aer.get_backend('aer_simulator')
    compiled = transpile(qc, sim)
    result = sim.run(compiled).result()

    return result.get_statevector()



def schrodinger_qiskit_sim(n_qubits, t=1.0, omega=1.0):

    qc = QuantumCircuit(n_qubits)
    qc.x(0)

    for i in range(n_qubits):
        qc.rz(-2 * omega * t, i)

    qc.save_statevector()
    sim = Aer.get_backend('aer_simulator')
    compiled = transpile(qc, sim)
    result = sim.run(compiled).result()
    return result.get_statevector()



def qaoa_qiskit_sim(n_qubits, p=1, gamma=0.5, beta=0.5):
    from qiskit import QuantumCircuit, transpile, Aer
    from numpy import pi

    qc = QuantumCircuit(n_qubits)

    qc.h(range(n_qubits))

    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            qc.cx(i, j)
            qc.rz(-2 * gamma, j)
            qc.cx(i, j)

    for i in range(n_qubits):
        qc.rx(2 * beta, i)

    qc.save_statevector()
    sim = Aer.get_backend("aer_simulator")
    compiled = transpile(qc, sim)
    result = sim.run(compiled).result()
    return result.get_statevector()
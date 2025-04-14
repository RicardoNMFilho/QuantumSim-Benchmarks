import cirq
import numpy as np

def qft_cirq_sim(n_qubits):
    qubits = cirq.LineQubit.range(n_qubits)
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[0]))

    for i in range(n_qubits):
        circuit.append(cirq.H(qubits[i]))
        for j in range(i+1, n_qubits):
            angle = np.pi / 2**(j - i)
            circuit.append(cirq.CZ(qubits[j], qubits[i])**(angle / np.pi))

    for i in range(n_qubits // 2):
        circuit.append(cirq.SWAP(qubits[i], qubits[n_qubits - i - 1]))

    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    return result.final_state_vector



def schrodinger_cirq_sim(n_qubits, t=1.0, omega=1.0):

    qubits = cirq.LineQubit.range(n_qubits)
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[0]))

    for q in qubits:
        circuit.append(cirq.rz(-2 * omega * t)(q))

    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    return result.final_state_vector



def qaoa_cirq_sim(n_qubits, p=1, gamma=0.5, beta=0.5):

    qubits = cirq.LineQubit.range(n_qubits)
    circuit = cirq.Circuit()

    circuit.append(cirq.H.on_each(*qubits))

    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            circuit.append(cirq.CNOT(qubits[i], qubits[j]))
            circuit.append(cirq.rz(-2 * gamma)(qubits[j]))
            circuit.append(cirq.CNOT(qubits[i], qubits[j]))

    for i in range(n_qubits):
        circuit.append(cirq.rx(2 * beta)(qubits[i]))

    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    return result.final_state_vector
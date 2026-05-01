from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit

def run_simulation(qc: QuantumCircuit, shots: int = 1024) -> dict:
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    result = job.result()
    return result.get_counts()
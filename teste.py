from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
print(result.get_counts())

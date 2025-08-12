from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

import matplotlib.pyplot as plt

# Cria circuito com 3 qubits e 2 bits clássicos
qc = QuantumCircuit(3, 2)

# Etapa 1: Prepara o estado a ser teletransportado (|+⟩)
qc.h(0)

# Etapa 2: Cria entrelaçamento entre q1 e q2
qc.h(1)
qc.cx(1, 2)

# Etapa 3: Aplica portas de Bell entre q0 e q1
qc.cx(0, 1)
qc.h(0)

# Etapa 4: Mede q0 e q1
qc.measure(0, 0)
qc.measure(1, 1)

# Etapa 5: Corrige q2 com base nas medidas
qc.cx(1, 2)
qc.cz(0, 2)

# Simula
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

# Visualiza
plot_histogram(counts)
plt.show()
print(qc.draw())



# 🧪 QuantumSim-Benchmarks

Este projeto tem como objetivo **comparar o desempenho e a implementação de algoritmos quânticos clássicos** em diferentes bibliotecas de simulação quântica:

- [Qiskit](https://qiskit.org/)
- [PennyLane](https://pennylane.ai/)
- [Cirq](https://quantumai.google/cirq)
- [QuTiP](https://qutip.org/)

## 🚀 Algoritmos Implementados

Cada algoritmo foi implementado em todos os frameworks com o mesmo número de qubits para análise justa. Os algoritmos incluídos até agora:

- ✅ **Quantum Fourier Transform (QFT)**
- ✅ **Schrödinger Equation (Time Evolution)**
- ✅ **Grover’s Search Algorithm**
- ✅ **Quantum Approximate Optimization Algorithm (QAOA)**
- ✅ **Bell Test (CHSH Inequality)**

Outros algoritmos podem ser adicionados futuramente.

## 🛠️ Estrutura do Projeto

```bash
QuantumSim-Benchmarks/
├── main.py                    # Script principal de execução e comparação
├── metrics.py                 # Função get_metrics para medir tempo de execução
├── qiskit_algorithms.py       # Algoritmos implementados com Qiskit
├── pennylane_algorithms.py    # Algoritmos implementados com PennyLane
├── cirq_algorithms.py         # Algoritmos implementados com Cirq
├── qutip_algorithms.py        # Algoritmos implementados com QuTiP
├── results/                   # Resultados e gráficos de benchmarks
└── README.md                  # Este arquivo
```

## 📊 Como os Benchmarks Funcionam

Cada função segue a assinatura `algoritmo_framework_sim(n_qubits)` e é avaliada pela função `get_metrics`, que calcula:

- Tempo de execução
- Estado final do sistema (ou valor final da métrica — ex: CHSH)

Exemplo de uso:

```python
from metrics import get_metrics
from qiskit_algorithms import qft_qiskit_sim

print(get_metrics(qft_qiskit_sim, 4))
```

---

## ⚙️ Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Certifique-se de que as seguintes bibliotecas estejam disponíveis:

- `qiskit`
- `pennylane`
- `cirq`
- `qutip`
- `matplotlib` (opcional para visualizações)
- `numpy`

---

## 📈 Exemplo de Resultado: CHSH

```text
Qiskit:    CHSH = 2.8284
PennyLane: CHSH = 2.8284
Cirq:      CHSH = 2.8284
QuTiP:     CHSH = 2.8284
```

Todos os frameworks retornam valores consistentes, demonstrando violação da desigualdade de Bell.

---

## 🧩 Contribuições Futuras

- Adição de mais algoritmos: VQE, Deutsch-Jozsa, Simon, etc.
- Suporte a mais simuladores (Braket SDK, Ocean SDK)
- Interface web para comparação visual
- Geração de gráficos automáticos de benchmark

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e contribuir.

---

## 👨‍💻 Autor

Desenvolvido por Ricardo Nogueira Miranda Filho — contribuições e sugestões são bem-vindas!

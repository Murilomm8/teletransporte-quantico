# 🧠 Teletransporte Quântico com Qiskit

Este projeto simula o famoso **teletransporte quântico** usando o framework [Qiskit](https://qiskit.org/).  
Você vai ver como o estado de um qubit pode ser transferido para outro, mesmo sem contato direto — usando entrelaçamento, medição e correções condicionais.

---

## 🚀 Objetivo

Demonstrar, de forma prática e visual, como funciona o protocolo de teletransporte quântico.  
O estado inicial do qubit `q0` (|+⟩) será transferido para o qubit `q2`, usando um par entrelaçado (`q1` e `q2`) e operações quânticas.

---

## 🧰 Requisitos

- Python 3.10+
- Ambiente virtual (recomendado)
- Pacotes:
  - `qiskit==0.46.0`
  - `qiskit-aer==0.12.0`
  - `matplotlib`

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/teletransporte-quantico.git
cd teletransporte-quantico
2. Crie e ative o ambiente virtual
bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
3. Instale os pacotes
bash
pip install -r requirements.txt
📄 Arquivos principais
main.py: Executa o circuito de teletransporte quântico e mostra o gráfico de medições

teste.py: Código de teste simples para verificar se o simulador Aer está funcionando

requirements.txt: Lista de dependências com versões compatíveis

🧪 Como rodar o experimento
bash
python main.py
Você verá um gráfico com os resultados das medições (00, 01, 10, 11) — cada combinação representa uma correção aplicada ao qubit q2.

📊 Interpretação do gráfico
Resultado	Correção aplicada a q2
'00'	Nenhuma
'01'	X
'10'	Z
'11'	X + Z
Essas correções garantem que q2 fique no mesmo estado que q0 estava originalmente — ou seja, o estado foi teletransportado!

🧠 Explicação do circuito
text
q0: ──H────■──H──M─────■──
           │      │    │
q1: ──H────X──────M────X──
                      │
q2: ───────X──────────X──
H: Hadamard (cria superposição)

CX: Porta de controle (entrelaçamento)

M: Medição

Correções condicionais: CX e CZ baseadas nos bits clássicos

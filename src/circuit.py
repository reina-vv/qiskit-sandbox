from qiskit import QuantumCircuit

def create_bell_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 0)
    qc.t(0)
    qc.measure([0, 1], [0, 1])
    return qc

def create_GHZ_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.measure_all()
    return qc

def deutsch_jozsa(oracle_type="balanced"):
    # 量子ビット2つ（q_0:入力、q_1:補助）、古典ビット1つ
    qc = QuantumCircuit(2, 1)

    # ① 補助ビットを |1⟩ に
    qc.x(1)

    # ② 両ビットにアダマール
    qc.h(0)
    qc.h(1)

    # ③ オラクル（関数の中身）
    if oracle_type == "balanced":
        qc.cx(0, 1)   # 平衡関数
    # constant の場合はここに何も置かない

    # ④ 入力ビットに再びアダマール
    qc.h(0)

    # ⑤ 測定
    qc.measure(0, 0)

    return qc

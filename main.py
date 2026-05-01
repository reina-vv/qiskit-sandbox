from src.circuit import *
from src.simulator import run_simulation
from src.utils import print_counts

def main():
    qc = deutsch_jozsa("balanced")
    counts = run_simulation(qc, shots=2048)
    print_counts(counts)
    print(qc.draw())

if __name__ == "__main__":
    main()
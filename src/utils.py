def print_counts(counts: dict) -> None:
    for state, count in sorted(counts.items()):
        print(f"|{state}⟩: {count}")
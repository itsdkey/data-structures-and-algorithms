from collections import defaultdict


def task2(libraries: list[dict]) -> dict:
    """Zbuduj strukture, ktora bedzie przechowywala wszystkie unikalne wersje
    oprogramowania dla danego komputera."""
    results = defaultdict(set)
    for library in libraries:
        softs = library["softs"]
        for computer, versions in softs.items():
            results[computer].update(versions)
    return results

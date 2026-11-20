from collections import Counter
def empirical_pmf(samples):
    if not samples:
        return []
    n = len(samples)
    counts = Counter(samples)
    return [(val, counts[val]/n) for val in sorted(counts)]
    pass
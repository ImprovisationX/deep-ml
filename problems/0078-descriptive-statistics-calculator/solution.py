import numpy as np
from collections import Counter
def descriptive_statistics(data: list | np.ndarray) -> dict:
    data = np.array(data, dtype=float)
    sorted_data = np.sort(data)
    mean = np.mean(data)
    median = np.median(data)
    counts = Counter(data)
    max_count = max(counts.values())

    mode = int(min(
        value for value, count in counts.items()
        if count == max_count
    ))


    variance = np.var(data)


    standard_deviation = np.std(data)

    p25 = np.percentile(data, 25)
    p50 = np.percentile(data, 50)
    p75 = np.percentile(data, 75)
    iqr = p75 - p25
    return {
        'mean': float(mean),
        'median': float(median),
        'mode': mode,
        'variance': float(variance),
        'standard_deviation': float(standard_deviation),
        '25th_percentile': float(p25),
        '50th_percentile': float(p50),
        '75th_percentile': float(p75),
        'interquartile_range': float(iqr)
    }
    pass
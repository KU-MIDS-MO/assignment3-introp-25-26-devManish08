import numpy as np

def moving_average(signal, window_size):
    a = len(signal)
    b = (window_size - 1) // 2
    final = np.zeros(a, dtype = float)

    for i in range(a):
        start = max(0, i - b)
        end = min(a, i + b + 1)
        final[i] = np.mean(signal[start:end])

    return final

import numpy as np

def count_values_in_bins(data, bin_edges):
    a = len(bin_edges) - 1
    count = np.zeros(a , dtype = int)

    for i in range(a):
        if i < a - 1:
            b = (data >= bin_edges[i]) & (data < bin_edges[i + 1])
        else:
            b = (data >= bin_edges[i]) & (data <= bin_edges[i + 1])

        count[i] = np.sum(b)

    return count

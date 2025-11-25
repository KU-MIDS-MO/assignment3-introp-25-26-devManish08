import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    clean = np.copy(scores)

    clean[clean < min_score] = min_score
    clean[clean > max_score] = max_score

    scaled = (clean - min_score) / (max_score - min_score)

    return scaled


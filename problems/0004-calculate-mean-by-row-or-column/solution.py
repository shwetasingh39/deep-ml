import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str):
	a = np.array(matrix)
    if mode=="row":
        means=np.mean(a, axis=1)
    else:
        means=np.mean(a, axis=0)
    
    means = means.tolist()  
    return means
# shop/recommender.pyx
import numpy as np
cimport numpy as cnp

# Ye function product scores calculate karta hai
def get_similarity_scores(cnp.ndarray[cnp.float64_t, ndim=1] user_vector, 
                          cnp.ndarray[cnp.float64_t, ndim=2] product_matrix):
    
    cdef int i, j
    cdef int num_products = product_matrix.shape[0]
    cdef int num_features = product_matrix.shape[1]
    
    # Result store karne ke liye array
    cdef cnp.ndarray[cnp.float64_t, ndim=1] scores = np.zeros(num_products)

    # Heavy calculation loop - Cython isse C ki speed pe chalayega
    for i in range(num_products):
        dot_product = 0
        for j in range(num_features):
            dot_product += user_vector[j] * product_matrix[i, j]
        scores[i] = dot_product
        
    return scores
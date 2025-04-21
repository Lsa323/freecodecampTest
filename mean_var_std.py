import numpy as np
#function named calculate()
def calculate(liste:list)-> list:
    if len(liste) != 9:
        raise ValueError('list must contain nine numbers')
    else:
        #convert into 3x3 array
        liste=np.array(liste).reshape(3, 3)
        calculValeur = {
            'mean':[liste.mean(axis=0).tolist(), liste.mean(axis=1).tolist(), liste.mean()],
            'variance':[liste.var(axis=0).tolist(),liste.var(axis=1).tolist(),liste.var()],
            'standard deviation' : [liste.std(axis=0).tolist(),liste.std(axis=1).tolist(),liste.std()],
            'max': [liste.max(axis=0).tolist(),liste.max(axis=1),liste.max()],
            'min': [liste.min(axis=0).tolist(),liste.min(axis=1),liste.min()],
            'sum': [liste.sum(axis=0).tolist(),liste.sum(axis=1),liste.sum()]
        }
        return calculValeur
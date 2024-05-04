import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    # Convertir la lista en una matriz de 3x3
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calcular las estadísticas requeridas
    mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
    variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
    std_deviation = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
    maximum = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
    minimum = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
    summation = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    
    # Construir el diccionario de resultados
    results = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': maximum,
        'min': minimum,
        'sum': summation
    }
    
    return results

print(calculate([0,1,2,3,4,5,6,7,8]))


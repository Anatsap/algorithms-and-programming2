import unittest

def get_increase_intervals(array):
    i = 0
    result = []
    for j in range(1, len(array)):
        if array[j - 1] <= array[j]:
            if j == len(array) - 1:
                result.append([i, j])
        
        else:
            if i != j - 1:
                result.append([i, j - 1])
        
            i = j
    

    return result

def get_decrease_intervals(array):
    i = 0
    result = []
    for j in range(1, len(array)):
        if array[j - 1] >= array[j]:
            if j == len(array) - 1:
                result.append([i, j])
        
        else:
            if i != j - 1:
                result.append([i, j - 1])
        
            i = j
    

    return result
array =  [1, 2, 3, 4, 3, 2, 5]

inc_interval = get_increase_intervals(array)
dec_interval = get_decrease_intervals(array)

    


print("Increasing interval: ", inc_interval )
print("Decreasing interval: ", dec_interval)


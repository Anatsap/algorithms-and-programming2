import unittest

def check_monotonic_array(array):
    is_increase = True
    is_decrease = True
    n = len(array)
    for i in range(0, n - 1):
        if array[i] >= array[i + 1]:
            is_increase = False
        elif array[i] <= array[i + 1]:
            is_decrease = False
    
    return is_increase or is_decrease


    



   
# print(check_monotonic_array([1, 2, 3, 4, 5]))
# print(check_monotonic_array([5, 4, 3, 2, 1]))
# print(check_monotonic_array([5, 9, 3, 2, 1]))
# print(check_monotonic_array([5, 9, 3, 11, 1]))
# print(check_monotonic_array([23, 56, 90, 102, 203, 290]))
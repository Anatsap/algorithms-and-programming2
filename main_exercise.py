import unittest


def check_monotonic_array(array):
    is_increase = True
    is_decrease = True
    uncorrect_in = []
    uncorrect_de = []
    n = len(array)
    for i in range(0, n - 1):
        
        if array[i] > array[i + 1]:
            
            is_increase = False
            uncorrect_in.append(i + 1)
            
    
        elif array[i] < array[i + 1]:
            
            is_decrease = False
            uncorrect_de.append(i + 1)
            
            
          
    return is_increase or is_decrease, uncorrect_in, uncorrect_de
    


# fail1 = check_monotonic_array([1, 5, 48, 30, 32, 90, 56, 100])
# print(fail1)

# fail2 = check_monotonic_array([67, 54, 48, 89, 78, 15, 14, 100])
# print(fail2)

# fail3 = check_monotonic_array([90, 101, 126, 126, 203])
# print(fail3)

#Розділена функція
# def fail_increase(array):
#     n = len(array)
#     uncorrect = []
#     for i in range(0, n - 1):
#         if array[i] >= array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]

#             uncorrect.append(i + 1)

#     return uncorrect


# def fail_decrease(array):
#     n = len(array)
#     uncorrect = []
#     for i in range(0, n - 1):
#         if array[i] <= array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]

#             uncorrect.append(i + 1)
        
#     return uncorrect






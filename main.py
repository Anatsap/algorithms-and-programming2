import math

def get_min_side(array, n):
    s = array[0] * array[1] * n
    left = round(math.sqrt(s))
    right = s
    while left <= right:
        side = (left + right)//2              
    
        if (side // array[0]) * (side // array[1]) < n:
            left = side + 1                
        elif (side // array[0]) * (side // array[1]) >= n:
            right = side - 1

    return side


array = [1000000000, 999999999]
n = 2

result = get_min_side(array, n)
print("The smallest side of the square for leaves: ", str(result))

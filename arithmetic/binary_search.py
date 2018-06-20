import math

# 二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7 ,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

# 列表长度为128，需要多少步才能找到

print(math.log(128, 2))
print(math.log(128 * 2, 2))
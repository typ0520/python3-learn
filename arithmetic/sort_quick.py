def quicksort(arr):
    if len(arr) < 2:
        return arr
    base=arr[0]
    low=[]
    high=[]
    for val in arr[1:]:
        if val <= base:
            low.append(val)
        else:
            high.append(val)
    # low = [i for i in arr[1:] if val <= base ]
    high = [i for i in arr[1:] if val > base ]
    return quicksort(low) + [base] + quicksort(high)

if __name__ == "__main__":
    arr=[5,9,1,7,5,3,6,8]
    print(quicksort(arr))
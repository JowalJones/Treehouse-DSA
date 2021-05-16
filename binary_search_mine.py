def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            return None

def verify (index):
    if index is not None:
        print("Item found at index: ", index)
    else:
        print("Item not found!")

list = [1, 2, 3, 4, 5, 6, 7]

result = binary_search(list, 7)

verify(result)

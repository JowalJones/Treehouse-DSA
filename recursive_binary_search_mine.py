
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            list = list[midpoint+1:]
            return recursive_binary_search(list, target)
        else:
            list = list[:midpoint]
            return recursive_binary_search(list, target)

def verify(result):
    print("Number found: ", result)

nums = [1,2,3,4,5,6,7]
res = recursive_binary_search(nums, 7)
verify(res)

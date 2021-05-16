
def linear_search (list, target):
    for i in range (0, (len(list))):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print ("number found at index ", index)
    else:
        print ("number not found!")

nums = [1,2,3,4,5]


result = linear_search(nums, 3)
verify (result)



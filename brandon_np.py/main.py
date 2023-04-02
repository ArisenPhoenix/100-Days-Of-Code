import numpy as np


def mult(d, v):
    return d * v


CALLBACKS = 0


def add(d, v):
    global CALLBACKS
    print("callbacks: ", CALLBACKS)
    print("d: ", d)
    print("v: ", v)
    return d + v


def merge_arrays(lists: list):
    values = []
    num_lists = len(lists)
    indices = len(lists[0])
    for index in range(indices):
        values.append([])
        for a_list in range(num_lists):
            current_item = lists[a_list][index]
            values[index].append(current_item)
    # print("Merged Values: ", values)
    return values


def nest_level(obj):
    # Not a list? So the nest level will always be 0:
    if type(obj) != list:
        return 0
    # Now we're dealing only with list objects:
    max_level = 0
    for item in obj:
        # Getting recursively the level for each item in the list,
        # then updating the max found level:
        max_level = max(max_level, nest_level(item))
    # Adding 1, because 'obj' is a list (here is the recursion magic):
    return max_level + 1


def for_loop(times, cb):
    for i in range(times):
        cb()
        

def call_back(arrays, current_array, num_items, array_type, value, levels, levels_done):
    global CALLBACKS
    CALLBACKS += 1
    
    if CALLBACKS > 19:
        return
    for item in range(num_items):
        current_item = arrays[current_array][item]
        array_type = type(current_item)
        if array_type == int or array_type == float or array_type == np.float64:
            print("type: ", array_type)
            print(current_item)
            return add(value, current_item)
        elif array_type == str:
            return current_item + " "
        else:
            return call_back(arrays, current_array, num_items, array_type, value, levels, levels_done+1)


def get_root_type(arrays, levels):
    new_type = arrays
    for _ in range(levels+1):
        new_type = new_type[0]
    return type(new_type)
    
            
def add_array_items(arrays):
    array_levels = nest_level(arrays)
    num_items = len(arrays[0])
    array_type = get_root_type(arrays, array_levels)
    print(array_type)
    values = []
    
    levels_completed = 0
    for array in range(len(arrays)):
        value = ""
        levels_completed += 1
        value = call_back(arrays, array, num_items, array_type, value, array_levels, levels_completed)
        values.append(value)
    print("added values: ", values)
    return values


arr = np.random.random((3, 3, 3))
arr0 = arr[0][0][0]
arr1 = arr[1][1][1]
arr2 = arr0 + arr1
data = add_array_items(merge_arrays(arr))
print(data)


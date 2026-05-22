from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    my_list.pop(index)
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    #1: understand what pop means.. my_list.pop(), removes last element my_list.pop(0) removes first element
    #2: remove n elements.. implies we need to call my_list.pop() n times... hence we need a loop
    #3: loops are used to repeat something n times, calling pop from inside the loop.
    #4: return the modified list (it's the same var since we mutated(changed) it. Lists are mutable in Python)
    for i in range(n):
        my_list.pop()
    return my_list


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))

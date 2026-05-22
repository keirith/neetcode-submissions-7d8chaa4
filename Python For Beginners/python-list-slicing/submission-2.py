from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    #print(my_list[-1]) #returns the last element of the list. == my_list([len(my_list) - 1])
    # new_list = []
    # for i in range(3):
    #     popped = my_list.pop()
    #     new_list.insert(0, popped)
    # return new_list
    return my_list[-3:] #start at 3rd element from end and go all the way to the end


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
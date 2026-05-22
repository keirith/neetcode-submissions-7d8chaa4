from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    #return my_list.append(elements) 
    #above doesnt work bc .append() adds the list elements as single element.
    #ex [1,2,3,[4,5]]
    #fix is to iterate through the elements one by one and add to my_list, then return my_list
    for num in elements:
        my_list.append(num)
    return my_list




# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))

# Exersice 1
# Write your function here

end = 101


def every_three_nums(start):
    if start <= 100:
        lst = list(range(start, end, 3))
        return lst
    else:
        return []


# Uncomment the line below when your function is done
print(every_three_nums(101))


# Exersice 2
# Write your function here
def remove_middle(lst, start, end):
    del lst[start:(end + 1)]
    return lst


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Exersice 3
# Write your function here
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item2) > lst.count(item1):
        return item2
    else:
        return item1


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Exersice 4
# Write your function here

def double_index(lst, index):
    if index >= len(lst):
        return lst
    lst[index] = 2 * lst[index]
    return lst


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# Exersice 5
# Write your function here
def middle_element(lst):
    if len(lst) % 2 == 0:
        return (lst[(len(lst) - 1) // 2] + lst[(len(lst) + 1) // 2]) / 2
    else:
        return lst[(len(lst) - 1) // 2]

    # Uncomment the line below when your function is done


print(middle_element([5, 2, -10, -4, 4, 5]))

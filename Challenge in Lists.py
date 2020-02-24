#Exersice 1
def append_sum(lst):
  for i in range(3):
    sum = lst[len(lst) -1] + lst[len(lst)-2]
    lst.append(sum)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Exersice 2
#Write your function here
def larger_list(lst1, lst2):
  if len(lst1)>len(lst2):
    return lst1[-1]
  elif len(lst2)>len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5,4,3,2,2,2,4], [-10, 2, 5, 10,2,2,2,2,2,2]))

#Exersice 3
#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 3, 2, 1, 2], 2, 3))

#Exersice 4
#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Exersice 5
#Write your function here
def combine_sort(lst1, lst2):
  lst3 = lst1+lst2
  lst3.sort()
  return lst3

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
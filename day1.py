def compare_lists(list1, list2):

  # Pair up the smallest number in the left list with the smallest number in the right list
  # then the second-smallest left number with the second-smallest right number, and so on.
  list1.sort()
  list2.sort()

  # Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
  total_distance = 0
  for i in range(len(list1)):
    current_distance = abs(list1[i] - list2[i])
    total_distance += current_distance

  return total_distance

print(compare_lists(list1=[3, 4, 2, 1, 3, 3], list2=[4, 3, 5, 3, 9, 3]))

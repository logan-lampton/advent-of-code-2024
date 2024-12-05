def reports(report_matrix):

  # a report only counts as safe if both of the following are true:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
  
  number_safe_reports = 0

  for level in report_matrix:
    increasing = False
    decreasing = False
    unsafe = False
    for i in range(1, len(level)):
      if level[i] > level[i - 1]:
        increasing = True
      elif level[i] < level[i - 1]:
        decreasing = True
      if not 0 < abs(level[i] - level[i - 1]) <= 3:
        unsafe = True
        break

    if increasing != decreasing and not unsafe:
      number_safe_reports += 1

  return number_safe_reports

print(reports(report_matrix=[[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]))
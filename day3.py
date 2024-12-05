def uncorrupt(mull_input):
  finding_mul = mull_input.split("mul(")
  numbers_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

  result = 0

  for segment in finding_mul:
    hit_comma = False
    comma_index = None
    first_number = None
    second_number = None

    for i in range(len(segment)):
      if not hit_comma:
        if segment[i] not in numbers_array:
            if segment[i] != ",":
              break
            if segment[i] == ",":
              first_number = int(segment[0: i])
              hit_comma = True
              comma_index = i
      else:
        if segment[i] not in numbers_array or i > comma_index + 3:
          if segment[i] == ")":
            second_number = int(segment[comma_index + 1: i])
            break
    
    # within each segment, at the end check if there is a valid first and second number. If so, multiply them together and add the product to the result.
    if first_number and second_number:
      cur_product = first_number * second_number
      result += cur_product

  return result

print(uncorrupt(mull_input="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))
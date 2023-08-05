def max_num(num1, num2, num3):
    return max([num1, num2, num3])

print(max_num(23, 4, 103))
print(max_num(34, 23, 12))
print(max_num(290, 463, 762))

def mult_list(lst):
  
  if len(lst) == 0:
    return 0
  
  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([44, 7, 12]))
print(mult_list([11, 99, 365]))
print(mult_list([15]))
    
def rev_string():
  my_str = "Hello, my name is Colin."
  my_str = my_str[::-1]
  return my_str

reverse_string = rev_string()
print(reverse_string)

def num_within(x, b, c):
  return x in range(b, c+1)

print(num_within(2, 3, 10))
print(num_within(5, 10, 7))
print(num_within(2, 1, 0))

triangle = [[1], [1, 1]]
def pascal(n):
	#base
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev) +1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)
    
pascal(2)
pascal(5)
                                                    
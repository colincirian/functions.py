def max_num(num1, num2, num3):
    return max([num1, num2, num3])

print(max_num(23, 4, 103))
print(max_num(34, 23, 12))
print(max_num(290, 463, 762))

def mult_list(lst):
  #if empty list, return 0
  if len(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))
    
#def rev_string():




#def num_within():



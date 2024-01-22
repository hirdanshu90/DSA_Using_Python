# Map a function over a list.....
nums = [1,2,3,4,5,6,7,8,9,10,11]

nums2 = [10,11,12,13,14,15,16,17,18]



def add(x, y):
  return x + y


add_values =  list( map(add,nums,nums2))

print(add_values)
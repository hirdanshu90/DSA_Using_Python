def increaseNumber(arr, index):

# Base case
  if index == len(arr)-1:
    return True

# logic
  if arr[index+1] - arr[index] < 0:
    return False
    
  return increaseNumber(arr, index+1)


index = 0
print(increaseNumber([3,5,7,12,55,58,100], index))
def printR (strr,ptr):
# Base case
  if ptr <0:
    return

# Print
  print(strr[ptr])

# Logic
  printR(strr,ptr-1)


strr= "abcdef"

print(printR(strr, len(strr)-1))
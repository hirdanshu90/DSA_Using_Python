def Recursion1 (i,n, sum):

# Base Case. 
  if i == n:
    sum += i
    return sum

# Work.
  sum = i+ sum
# Recursion
  return Recursion1(i+1,n,sum)




print(Recursion1(0,5,0))
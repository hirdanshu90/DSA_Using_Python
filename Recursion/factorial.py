def factorial(n):

  # Base case. 
  if n == 1 or n==0:
    return 1
  # Work
  facto = n*factorial(n-1)
  # Return
  return facto




print(factorial(6))
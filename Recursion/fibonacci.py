def fibo(a,b,n):

# Base case
  if n == 0:
    return 
  
# Logic
  c= a+b
# Print no
  print(c)
  
# Return
  return fibo(b,c,n-1)


print(fibo(0,1,7))
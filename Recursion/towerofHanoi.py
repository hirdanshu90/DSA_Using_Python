def towerofHanoi(n, src, helper, dest):

  # Base case
  if n == 1:
    print("Transferring from " + str(n) + " from " + src + " to " + dest)
    return 

  # Logic .......

  #  transfer n-1 discs first, then the last one ...... 
  # Time Complexity: O(2^n-1) steps. 

  # Transfering n-1 discs from src to helper tower.
  towerofHanoi(n-1, src, dest, helper)

  # print, transfer is happening ...
  print("Transferring from " + str(n) + " from " + src + " to " + dest)

  # Transfering n-1 discs from helper to dest tower.
  towerofHanoi(n-1, helper, src,dest)
  
  return


print(towerofHanoi(3,"S", "H", "D"))
# Initial index value taken -1, basically not in the index range. 

first = -1
last = -1

def firstLastOccur(strr, idx,element):
  global first
  global last
  # Base case
  if idx == len(strr):
    print(first)
    print(last)
    print(strr[last])
    return

  # Logic
  if strr[idx] == element:
    if first == -1:
      first = idx

    else:
      last = idx

# Return.
  firstLastOccur(strr, idx+1, element)


print(firstLastOccur("adaakaf",0 , "a"))


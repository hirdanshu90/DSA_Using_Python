# Binary search algorithm.

# Integer overflow occurs when the result of an arithmetic operation exceeds the maximum value that can be represented by the data type being used. In most programming languages, integers have a fixed size (e.g., 32 bits or 64 bits), which means they can only hold values within a specific range.

# For example, in a typical 32-bit signed integer in many programming languages, the maximum representable value is 2,147,483,647. If you attempt to perform an addition operation that results in a value greater than this, an integer overflow occurs. When overflow happens, the value wraps around, often resulting in unexpected and incorrect behavior.

# In the context of the binary search algorithm, overflow can occur if the indices left and right are large enough to cause their sum to exceed the maximum representable value for the integer data type. For instance, consider the expression mid = left + (right - left) // 2. If left and right are both large integers, the subtraction right - left could result in a value close to the maximum representable integer value. Adding this value to left may lead to an overflow situation.

# To prevent integer overflow, it's crucial to choose appropriate data types or use techniques like checking for potential overflow before performing arithmetic operations. Languages like Python automatically handle arbitrary-precision arithmetic, meaning integers can grow as large as the available memory allows, mitigating the risk of overflow. However, in languages with fixed-size integers, developers need to be cautious about potential overflow issues and design their algorithms accordingly.

def binary_search (arr, item):

  left = 0
  right = len(arr) -1

  while left < right:
    mid = left + (right - left)//2

    if item == arr[mid]:
      return "Value is present"
    
    elif item > arr[mid]:
      left = mid + 1

    else:
      right = mid - 1


  return "Value not present"


arr = [3,6,7,9,12,22,44,56,76,98,101]
item = 73

print(binary_search(arr, item))
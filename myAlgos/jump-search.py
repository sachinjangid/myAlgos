#User function Template for python3
import math

def jumpSearch(arr, number, n):
  jump = (math.sqrt(n))
  prev = 0 
  while (arr[int(min(jump,n)-1)] < number):
    prev = jump
    jump = jump + math.sqrt(n)
    if (prev >= n):
      return -1
  prev = int(prev)
  while (arr[int(prev)] < number):
    prev = prev + 1 
    if (arr[prev] == number):
      return prev
    if (prev > min(jump,n)):
      return -1
  if (arr[int(prev)] == number):
    return prev
  return -1
    


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        params=[int(x) for x in input().strip().split()]
        n = params[0]
        number = params[1]
        arr=[int(x) for x in input().strip().split()]
        result = jumpSearch(arr, number, n)
        if (result > -1):
          print(result+1)
        else:
          print(result)


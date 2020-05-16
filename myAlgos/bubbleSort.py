def bubbleSort(arr):
  doSort = True
  swapped = False
  index = 0
  while doSort and index < (len(arr)-1):
    if (index == 0):
      swapped = False
    if (arr[index] > arr[index+1]):
      arr[index+1], arr[index] = arr[index], arr[index+1]
      swapped = True
    index += 1
    if (index ==(len(arr)-1)) and swapped:
      index = 0
    elif (index ==(len(arr)-1)) and not swapped:
      doSort = False
  return arr
  

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        arr=[int(x) for x in input().strip().split()]
        result = bubbleSort(arr)
        print(result)


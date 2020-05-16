def selectionSort(arr):
  for i in range(len(arr)):
    minIndex = i
    for j in range(i+1, len(arr)):
      if arr[minIndex] > arr[j]:
        minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
  return arr


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        arr=[int(x) for x in input().strip().split()]
        result = selectionSort(arr)
        print(result)


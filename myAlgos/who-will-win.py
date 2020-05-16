#User function Template for python3


def binarySearch(arr, number, initial, end):
    if (end >= initial):
      middle = initial + (end - initial) // 2

      if arr[middle] == number:
        return middle
      elif (number > arr[middle]):
        print("for next itiraration",middle, end)
        return binarySearch(arr, number, middle+1, end)
      else:
        print("for next itiraration",initial, middle-1)
        return binarySearch(arr, number, initial, middle-1)
    else:
      return -1



if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        params=[int(x) for x in input().strip().split()]
        n = params[0]
        number = params[1]
        arr=[int(x) for x in input().strip().split()]
        result = binarySearch(arr, number, 0, n-1)
        if (result > -1):
          print(result+1)
        else:
          print(result)


def getShortestIndex(arr, totalSum):
    n = len(arr)
    initialIndex = 0
    lastIndex = 0

    gotIndex = 0
    for i in range(n):
      initialIndex = i
      currentSum  = 0

      nextIndex = i
      while (currentSum < 12 and nextIndex < n -1):
        currentSum += arr[nextIndex]
        if (currentSum == totalSum):
          lastIndex = nextIndex
          gotIndex = 1
          break
        nextIndex += 1
      if (gotIndex == 1):
        break
    if (gotIndex == 1):
      print(initialIndex + 1, lastIndex + 1)
    else:
      print(-1)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        r=[int(x) for x in input().strip().split()]
        n = r[0]
        totalSum = r[1]
        arr=[int(x) for x in input().strip().split()]
        getShortestIndex(arr, totalSum)

# } Driver Code Ends
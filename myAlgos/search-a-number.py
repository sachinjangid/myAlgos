#User function Template for python3


def searchNumber(arr,n, number):
    index = -1
    for i in range(n):
      if (arr[i] == number):
        index =i
        break
    if (index > -1):
      print(index+1)
    else:
      print(index)



if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        params=[int(x) for x in input().strip().split()]
        n = params[0]
        number = params[1]
        arr=[int(x) for x in input().strip().split()]
        n = len(arr)
        arr[311] = 367
        arr[319] = 367
        searchNumber(arr,n, number)


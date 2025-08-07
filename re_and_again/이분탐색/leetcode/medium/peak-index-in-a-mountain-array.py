'''
배열 중 정점을 찾는 문제 하나의 정점이 있는 것이 보장된다.
O(log n)으로 풀어야 한다. -> 이분 탐색 접근

left, right = 0, n-1 초기화.

arr[mid] < arr[mid+1] 인 유일한 부분을 찾아야함
위 조건의 경우 올라가는 중인 것이고, 아닐 경우 내려가는 중이니까.
이분 탐색으로 범위를 줄이다가 left > right가 되는 경우가 유일한 정점인 케이스이다.

처음 접근이 맞았는데 왜 틀렸냐 하면
if arr[mid] < arr[mid+1] 가 아닐 때,
right = mid + 1을 했다.
탐색 범위에 mid를 제외하면 안되었는데, 내가 잘 못 생각했다.
다음부터 이분 탐색일 때 특정 조건의 구간을 찾는 문제가 나온다면 mid를 제외하지 않도록 조심해야겠다.

'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left
'''
숫자를 이진수로 표현하고, 이를 트리로 나타냈을 때, 그리고 빈 공간을 0으로 채웠을 때,
정수가 실제로 표현가능한 이진트리로 표현되는지 확인하는 문제
ex) 2 -> 10 -> 010 -> 1
                     / \
                    0   0

ex) 5 -> 101 -> 0
               / \
              1   1
=> 존재하는 노드의 부모 노드가 존재하지 않음(0)이므로 표현 불가능
              

1 ≤ numbers의 길이 ≤ 10,000
1 ≤ numbers의 원소 ≤ 10^15
-> O(n log(n)) 풀이 가능


1. 일단 포화 이진트리로 변환한다.
    1-1. 십진수를 이진수로 표현하고
        1-1-1. 이진수로 나타냈을 때 포화 이진트리가 되지 않으면, 포화이진트리가 되도록 앞에 0을 채워준다.
               해당 트리가 포화이진트리가 되었을 때의 노드 개수 = 2 ** (math.floor(math.log2(len(tree))) + 1) -1
2. 포화 이진트리의 양 서브트리를 DFS로 순회한다.
    ex) DFS(tree[mid]), DFS(tree[:mid+1])
    서브트리를 순화할 때, 부모노드가 0인데, 자식의 루트노드가 1인 경우, 표현이 불가능한 노드이기 때문에,
    (tree[mid] == '0' and not left) or (tree[mid] == '0' and not right)의 경우 해당 번호의 answer를 0으로 바꾼다.
3. answer를 리턴한다.

'''

import math
def solution(numbers):
    answer = [1 for _ in range(len(numbers))]
    
    def dfs(tree, i):
        mid = len(tree) // 2
        
        if len(tree) > 1:
            left = dfs(tree[:mid], i)
            right = dfs(tree[mid+1:], i)
            
            if (tree[mid] == '0' and not left) or (tree[mid] == '0' and not right):
                answer[i] = 0
                
        return tree[mid] == '0'
    
    for i, n in enumerate(numbers):
        tree = bin(n)[2:]
        
        more = 2 ** (math.floor(math.log2(len(tree))) + 1) -1
        for _ in range(len(tree), more):
            tree = '0' + tree

        tree = list(tree)
        dfs(tree, i)
    return answer
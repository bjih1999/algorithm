from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

post_answer = []
pre_answer = []

'''
시간 복잡도 O(k). k는 트리의 depth. k < 1000
'''
def preorder(x_list, y_list):
    global pre_answer
    
    root = y_list[0]
    pivot = x_list.index(root)

    left_y = []
    right_y = []
    
    for i in range(1, len(y_list)):
        if y_list[i][0] < root[0]:
            left_y.append(y_list[i])
        else:
            right_y.append(y_list[i])
    
    pre_answer.append(root[2])
    if left_y:
        preorder(x_list[:pivot], left_y)
    if right_y:
        preorder(x_list[pivot + 1:], right_y)

def postorder(x_list, y_list):
    global post_answer
    
    left_y = []
    right_y = []
    
    # 현 서브 트리의 루트
    root = y_list[0]
    
    # root 기준으로 x_list 분할하기 위해 root의 인덱스를 구함
    pivot = x_list.index(root)
    
    # 지금 트리에 포함된 node들을 root 기준 좌우로 분할
    for i in range(1, len(y_list)):
        if y_list[i][0] < root[0]:
            left_y.append(y_list[i])
        else:
            right_y.append(y_list[i])
    
    # 왼쪽 트리가 있으면 왼쪽 서브 트리로 재귀
    if left_y:
        postorder(x_list[:pivot], left_y)
    
    # 오른쪽 트리가 있으면 오른쪽 서브 트리로 재귀
    if right_y:
        postorder(x_list[pivot+1:], right_y)
    
    post_answer.append(root[2])
    
    
def solution(nodeinfo):
    global post_answer, pre_answer

    # node에 번호 붙이기
    node_list = []
    for index, node in enumerate(nodeinfo):
        x, y = node
        node_list.append((x, y, index+1))
    
    # x 좌표 오름차순 정렬
    list_x = sorted(node_list)
    # y 좌표 내림차순 정렬
    list_y = sorted(node_list, key=lambda x: (-x[1], x[0]))

    postorder(list_x, list_y)
    preorder(list_x, list_y)
    
    return pre_answer, post_answer
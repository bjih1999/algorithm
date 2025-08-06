# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
개쩌는 트리 구조 탐색하는 법
일케 하면 트리 구조를 튜플로 만들 수 있음
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def test(node):
            return node and (node.val, test(node.left), test(node.right))

        return test(p) == test(q)
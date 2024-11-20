'''
n개의 괄호로 이루어진 올바른 문자열 찾기
n = 8에 O(2^n) 풀이(depth가 최대 8인 트리 완전 탐색)

닫는 괄호는 여는 괄호보다 적을 때만 추가하기
여는 괄호는 총 괄호 개수만큼만 추가하기
로 dfs 탐색
'''

class Solution:
    answer_set = set()
    def dfs(self, current, opened, closed, n):
        if opened >= n and closed >= n:
            self.answer_set.add(current)
            return
        
        if closed < opened:
            self.dfs(current + ')', opened, closed + 1, n)
        
        if opened < n:
            self.dfs(current + '(', opened + 1, closed, n)


    def generateParenthesis(self, n: int) -> List[str]:
        self.answer_set = set()
        self.dfs('', 0, 0, n)

        return list(self.answer_set)
        
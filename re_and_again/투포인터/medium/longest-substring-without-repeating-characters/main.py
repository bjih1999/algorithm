'''
겹치는 문자가 없이 가장 긴 substring의 길이를 구하는 문제

투포인터를 사용하여 O(n)으로 풀이함.
0 <= s.length <= 5 * 10^4

r과 l 사이에 있는 문자열을 set에 저장하여 중복 검사를 O(1)로 할 수 있게 함.
l을 증가시키며 새로 추가할 문자가 set에 존재하는지 확인함. 이 때 set의 길이(문자열의 길이)의 최댓값을 확인하고 갱신함.
만약 중복되는 문자가 있다면 r이 가리키는 문자를 set에서 제거함. 그리고 r을 1 증가시킴.

이 작업을 l < n , r < n 일 때까지 반복함. ( O(2 * s.length) )
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        r = 0
        l = 0
        n = len(s)
        not_duplicated = set()

        while r < n and l < n:
            if s[r] not in not_duplicated:
                not_duplicated.add(s[r])
                result = max(result, r - l + 1)
                r += 1
            else:
                not_duplicated.remove(s[l])
                l += 1
        
        return result
        
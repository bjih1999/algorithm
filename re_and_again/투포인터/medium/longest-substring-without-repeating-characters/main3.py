'''
투포인터와 문자가 마지막으로 발견된 위치를 dict에 저장하여 중복이 발생할 경우, left를 중복 문자열 이후로 점프시켜 중복 없이 길이를 계산하는 방법
이 때 단순히 left = last_position[c]를 하는 경우 left가 뒤로 돌아가 타 문자와 중복이 발생할 수 있기 때문에 left = max(left, last_position[c])로 left가 역행하는 상황을 방지한다.

시간 복잡도는 O(N) => O( 2 * s.length ) => O( 2 * 5 * 10^4 )
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_position = {}
        left = 0
        result = 0
        
        for right, c in enumerate(s):
            
            # 만약 중복되는 문자가 있다면 left를 그 문자 다음으로 옮긴다.
            if c in last_position:
                left = max(left, last_position[c] + 1)
            
            last_position[c] = right
            result = max(result, right - left + 1)
        
        return result
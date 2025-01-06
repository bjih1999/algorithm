'''
투포인터에 해시를 사용한 풀이.
s right로 순회하며 여태 발견된 문자의 개수를 dict에 저장함.
만약 현재 문자의 개수가 2 이상이라고 하면, left를 증가시키며 left에 해당하는 문자의 개수를 하나씩 줄임.
위 수행을 right의 개수가 2 이하가 될 때까지 수행함.
left가 가리키는 문자의 개수를 하나씩 줄이고 left를 이동시켰는데, right가 가리키는 문자의 개수가 2 이하가 되었다는 의미는 중복이 없어졌다는 이유이기 때문임.

위 수행을 s의 길이만큼 수행함.

시간 복잡도는 최악의 경우 모든 문자를 2번씩 참조하기 때문에 O(N) => O(2 * s.legnth) => O( 2 * 5 * 10^4 ) 이다.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = {}
        left = 0
        result = 0
        for right, c in enumerate(s):

            count[c] = 1 + count.get(c, 0)

            while count[c] > 1 and left < right:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result
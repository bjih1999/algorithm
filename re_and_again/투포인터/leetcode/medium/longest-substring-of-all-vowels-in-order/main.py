'''
아래 조건을 만족할 때 문자열이 beautiful하다고 할 수 있음.
1. 문자열에 'a', 'e', 'i', 'o', 'u'가 모두 포함되어야함
2. 문자열이 'a', 'e', 'i', 'o', 'u'가 알파벳 순서대로 정렬되어있어야함.

주어진 문자열 word의 substring 중 beautiful하고 가장 긴 substring의 길이를 리턴해야함.

1 <= word.length <= 5 * 10^5 => log n 이하 풀이 필요. => 투포인터로 풀임

풀이)
1. 알파벳 순서대로 모음들을 1, 2, 3, 4, 5로 매핑함.
2. i = 문자열의 시작, j = 문자열의 끝. j = i+1로 시작하고, j를 늘려가며 하나씩 배열의 크기가 1씩 증가하는지 혹은 값이 변동이 없는지 확인
    2-1. j가 1이상 증가한 경우 i = j, j += 1을 하며 문자열을 뛰어넘어 버린다.
    2-2. j가 0~1씩 증가하다가 translated[j] == 5, translated[i] == 1인 경우 answer을 j-i+1로 max 갱신함.
        위조건을 만족한 경우 a~u를 모두 포함하고 알파벳 순서대로 정렬이 된 상태이기 때문

3. answer를 리턴함
'''

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        score = {
            'a':1,
            'e':2,
            'i':3,
            'o':4,
            'u':5
        }

        translated = []
        n = len(word)
        for letter in word:
            translated.append(score[letter])
        
        answer = 0
        
        i = 0
        j = 1
        while j < n:
            
            if translated[j] == translated[j-1] or translated[j] == translated[j-1] + 1:
                
                if translated[i] == 1 and translated[j] == 5:
                    answer = max(answer, j-i + 1)
            else:
                i = j
            
            j += 1

    
        return answer

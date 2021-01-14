/**
 * "124 나라의 숫자"
 * 
 * 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
 * 124 나라에는 자연수만 존재합니다.
 * 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
 * 
 * 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
 * 
 * https://programmers.co.kr/learn/courses/30/lessons/12899
 * 
 */

class Solution {
	public String solution(int n) {
		String answer = "";
		StringBuilder sb = new StringBuilder();
		int remainder = 0;

		while(n > 0){			
			remainder = n%3;
			n = n/3;
			if(remainder == 0){
				n = n - 1;
				remainder = 4;
			}
			sb.insert(0, remainder);
		}
		answer = sb.toString();
		return answer;
	}
}
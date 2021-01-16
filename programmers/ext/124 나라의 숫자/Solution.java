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
import java.util.ArrayList;

class Solution {
	public String solution(int n) {
		String answer = "";

		StringBuilder sb = new StringBuilder();
		ArrayList<String> arr = new ArrayList<>();
		int quotient = 0;
		int remainder = 0;
		int digit1 = 0;
		arr.add("0");
		for(int i = 1 ; i <= n ; i++){
			quotient = i / 3;
			remainder = i % 3;
			if(remainder == 0){
				digit1 = 4;
			}
			else{
				digit1 = remainder;
			}

			if(remainder == 0){
				sb.append(arr.get(quotient-1));
				sb.append(digit1);
				arr.add(i, sb.toString());
				sb = new StringBuilder();
			}
			else{
				sb.append(arr.get(quotient));
				sb.append(digit1);
				arr.add(i, sb.toString());
				sb = new StringBuilder();
			}
		}
		answer = sb.append(Long.parseLong(arr.get(n))).toString();
		sb = new StringBuilder();
		return answer;
	}
}
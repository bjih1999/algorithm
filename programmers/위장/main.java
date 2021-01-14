public class main {
	public static void main(String[] args){
		Solution solution = new Solution();
		String[][] str1 = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
		System.out.println(solution.solution(str1));

		String[][] str2 = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
		System.out.println(solution.solution(str2));
	}
}

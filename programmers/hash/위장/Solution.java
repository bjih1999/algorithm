/**
 * �����̵��� ���� �ٸ� ���� �����Ͽ� �Ծ� �ڽ��� �����մϴ�.

���� ��� �����̰� ���� ���� �Ʒ��� ���� ���� �����̰� ���׶� �Ȱ�, �� ��Ʈ, �Ķ��� Ƽ������ �Ծ��ٸ� �������� û������ �߰��� �԰ų� ���׶� �Ȱ� ��� ���� ���۶󽺸� �����ϰų� �ؾ� �մϴ�.
�����̰� ���� �ǻ���� ��� 2���� �迭 clothes�� �־��� �� ���� �ٸ� ���� ������ ���� return �ϵ��� solution �Լ��� �ۼ����ּ���.

https://programmers.co.kr/learn/courses/30/lessons/42578?language=java
 */

import java.security.KeyStore;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

class Solution {
    public int solution(String[][] clothes) {
		int answer = 1;
		HashMap<String, Integer> hashMap = new HashMap<>();

		for(int i = 0 ; i < clothes.length ; i++){
			if(!hashMap.containsKey(clothes[i][1])){
				hashMap.put(clothes[i][1], 1);
			}
			else{
				hashMap.put(clothes[i][1], (hashMap.get(clothes[i][1]).intValue()) + 1);
			}
		}
		for(String key : hashMap.keySet()){
			answer *= (hashMap.get(key)+1);
		}
        return answer-1;
    }
}
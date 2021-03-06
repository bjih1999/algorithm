/**
 * 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

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
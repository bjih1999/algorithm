/**
 * 로마 숫자를 정수로 변환하기
 * IV -> 4와 같은 경우가 변수인데,
 * 숫자를 계속 변환하여 stack에 저장하다가, stack.peek() 보다 현재 로마숫자가 크면, 뺄셈을 해야하는 상황으로 인식하고,
 * 현재보다 작은 숫자가 없을 때까지 pop()을 함. 그리고 그 pop()된 숫자의 합을 현재 로마숫자에 뺀 값을 stack에 넣음
 * 
 */

import java.util.*;

class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> board = new HashMap<>();
        board.put('I', 1);
        board.put('V', 5);
        board.put('X', 10);
        board.put('L', 50);
        board.put('C', 100);
        board.put('D', 500);
        board.put('M', 1000);
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < s.length() ; i++) {
            char current = s.charAt(i);
            int value = board.get(current);
            int deductAmount = 0;
            while (!stack.isEmpty() && stack.peek() < value) {
                deductAmount += stack.pop();
            }
            stack.add(value - deductAmount);
        }

        return stack.stream().mapToInt(i->i).sum();
    }
}
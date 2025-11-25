import java.util.*;

class Solution {
    public int clumsy(int n) {
        Stack<Integer> stack = new Stack<>();

        for (int i = n ; i > 0 ; i--) {
            int j = n - i;

            if (j == 0) {
                stack.add(n);
                continue;
            }

            if (j % 4 == 0) {
                stack.add(i * -1);
            } else if (j % 4 == 1) {
                int current = stack.pop();
                stack.add(current * i);
            } else if (j % 4 == 2) {
                int current = stack.pop();
                stack.add((int) current / i);
            } else {
                stack.add(i);
            }
        }

        int result = 0;
        for (int s: stack) {
            result += s;
        }
        
        return result;
    }
}
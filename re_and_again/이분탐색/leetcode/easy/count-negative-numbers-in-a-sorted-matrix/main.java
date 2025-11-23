/**
 * 
 * 이분 탐색을 활용한 lower bound.
 * right를 배열 length 대로 초기화해둠.
 * lower bound가 끝난 right == 조건을 만족하는 원소의 다음 인덱스
 */

import java.util.*;

class Solution {
    
    public int countNegatives(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int answer = 0;
    
        for (int i = 0 ; i < n ; i++) {
            
            int left = 0;
            int right = m;
            int[] current = Arrays.stream(grid[i]).sorted().toArray();
            while (left < right) {
                int mid = (int) (left + right) / 2;
                if (current[mid] < 0) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            answer += right;

        }

        return answer;
    }
}
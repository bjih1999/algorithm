/**
 * 배열로 주어진 모든 수의 모든 소인수의 개수를 구하시오.
 * 
 * 소인수 분해 알고리즘으로 소인수를 구함.
 * 소인수의 개수를 셈.
 * 
 * 1 <= n < 10**4
 * 2 <= nums[i] < 1000;
 * 
 * => O(10^7) 풀이
 */

import java.util.*;

class Solution {
    public int distinctPrimeFactors(int[] nums) {
        Set<Integer> result = new HashSet<>();

        for (int n: nums) {
            int current = n;
            for (int i = 2 ; i <= n ; i++) {

                while (current % i == 0) {
                    result.add(i);
                    current /= i;
                }
            }
        }

        return result.size();

    }
}
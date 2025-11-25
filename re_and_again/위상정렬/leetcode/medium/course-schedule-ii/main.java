/**
 * 대표적인 위상정렬 문제
 * indegrees가 0이 아닌 것이 있는 경우 성립이 불가능 하다는 것을 의미하기에 [] 리턴.
 * 그게 아닐 경우 위상정렬된 순서 중 하나 리턴
 * 
 */

import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer> answer = new LinkedList<>();
        
        List<Set<Integer>> board = new ArrayList<Set<Integer>>();
        int[] indegrees = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0 ; i < numCourses ; i++) {
            board.add(new HashSet<Integer>());
        }

        for (int[] p: prerequisites) {
            int a = p[0];
            int b = p[1];

            board.get(b).add(a);
            indegrees[a] += 1;
        }

 
        for (int i = 0 ; i < numCourses ; i++) {
            if (indegrees[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();
            answer.add(current);
            for (int next: board.get(current)) {
                indegrees[next]--;
                if (indegrees[next] == 0) {
                    queue.add(next);
                }
            }
        }

        if (Arrays.stream(indegrees).filter(i -> i != 0).count() !=0) {
            return new int[]{};
        }

        return answer.stream().mapToInt(i->i).toArray();
    }
}
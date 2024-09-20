import java.util.*;


class Solution {
    
    public int dfs(int[] visited, int[] cards, int current, int count) {
        if (visited[current] != 0) {
            return count;
        }
        // System.out.println(current);
        visited[current] = 1;
        int next = cards[current-1];
        return dfs(visited, cards, next, count + 1);
    }
    
    public int solution(int[] cards) {
        int answer = 0;
        int n = cards.length;
        List<Integer> scoreList = new ArrayList<>();
        int[] visited = new int[n+10];
        int[] board = new int[n+10];
        
        for (int i = 1; i <= n ; i++) {
            if (visited[i] == 0) {
                int count = dfs(visited, cards, i, 0);
                scoreList.add(count);
            }
        }
        scoreList.sort(Collections.reverseOrder());
        if (scoreList.size() <= 1){
            return 0;
        }
        answer = scoreList.get(0) * scoreList.get(1);
        return answer;
    }
}